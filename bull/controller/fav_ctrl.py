#!/usr/bin/python  
# -*- coding: utf-8 -*-
from PyQt4 import QtCore
from view.wrapper_factory import WrapperFactory
from view.qnew_fav_dlg import QNewFavDlg

class FavCtrl(QtCore.QObject):
    def __init__(self,wrapper_id,main_ctrl,dao,setting):
        self.wrapper_id = wrapper_id
        self.main_ctrl = main_ctrl
        self.fav_dao = dao
        self.setting = setting
        self.fav_list = self.fav_dao.load_fav()
        self.screener_listen_status = False
        wrapper_factory = WrapperFactory(setting)
        wrapper_kwargs = {
            'wrapper_id':wrapper_id,
            'main_window':main_ctrl.main_window,
            'dao':dao,
        }
        self.fav_wrapper = wrapper_factory.create_wrapper(**wrapper_kwargs)
        #响应fav_wrapper的点击消息
        self.connect(self.fav_wrapper,
            QtCore.SIGNAL('nth_click(int)'),
            self.on_nth_fav_click)
        #响应fav_wrapper的关闭消息
        self.connect(self.fav_wrapper,
            QtCore.SIGNAL('nth_close(int)'),
            self.on_nth_close)
        #响应main_ctrl的取消消息
        self.connect(self.main_ctrl,
            QtCore.SIGNAL('cancel_event()'),
            self.on_cancel_event)
        #响应main_ctrl的新建收藏消息
        self.connect(self.main_ctrl,
            QtCore.SIGNAL('new_fav_event()'),
            self.on_new_fav_event)
        #响应main_ctrl的保存收藏消息
        self.connect(self.main_ctrl,
            QtCore.SIGNAL('save_event()'),
            self.on_save_event)

    def set_wrapper_visible(self,status):
        self.fav_wrapper.setVisible(status)

    def get_condition(self):
        fav = self.get_fav_by_id(self.current_favid)
        return fav['condition']

    def set_condition(self,condition):
        self.set_fav(self.current_favid,condition)

    def set_fav(self,favid,condition_list):
        idx = self.find_idx_by_id(favid)
        self.fav_list[idx]['condition']=condition_list
        self.fav_dao.store_fav(self.fav_list)
    
    def find_idx_by_id(self,favid):
        return [item['favid'] for item in self.fav_list].index(favid)   

    def find_fav_by_id(self,favid):
        idx =  self.find_idx_by_id(favid)
        return self.fav_list[idx]

    def delete_fav_by_id(self,favid):
        idx = self.find_idx_by_id(favid)
        self.fav_list.pop(idx)
        self.fav_dao.store_fav(self.fav_list)

    def new_fav(self,title,condition_list):
        new_fav_id = self.gen_new_id()
        new_fav_item = {
            'screener':self.get_screener_id(),
            'favid':new_fav_id,
            'condition':condition_list,
            'title':unicode(title),
        }
        self.fav_list.append(new_fav_item)
        self.fav_dao.store_fav(self.fav_list)
        try:
            self.view.fav_wrapper.add_fav_item(new_fav_item)
        except:
            pass

    #这是用来生成新fav的id的, 并不适用与找当前最大的id
    def gen_new_id(self):
        if len(self.fav_list)==0:
            return 0;
        else:
            return max([item['favid'] for item in self.fav_list])+1

    #保存当前对此收藏的改动
    def on_save_event(self):
        if self.screener_listen_status == False:
            return
        condition = self.main_ctrl.screener_group_ctrl.get_condition()
        self.set_fav(self.current_favid,condition)

    #取消当前的收藏状态, 转为没有收藏的状态
    def on_cancel_event(self):
        if self.screener_listen_status == False:
            return
        self.main_ctrl.screener_group_ctrl.reset_button_group()
        self.main_ctrl.screener_group_ctrl.reset_header()
        self.screener_listen_status = False
        self.main_ctrl.set_save_transmit('new_fav_event()')
        self.main_ctrl.set_cancel_transmit('reset_event()')

    #新建一个fav,
    def on_new_fav_event(self):
        dlg_data = {
            'title':self.setting['new_fav_dlg_title'],
            'setting':self.setting,
        }
        dlg = QNewFavDlg(self.view,dlg_data)
        dlg.exec_()
        value = dlg.get_value()
        if value != None and value != False:
            condition_list = self.get_condition_list()
            fav_ctrl = self.view.fav_ctrl
            fav_ctrl.new_fav(unicode(value),condition_list)

    #响应某一个收藏被删除的信号
    def on_nth_close(self,_id):
        #这里要try, 因为一开始的时候,current_favid可能还没设置
        try:
            if _id == self.current_favid:
                self.on_cancel_event()
        except:
            pass

        self.delete_fav_by_id(_id)

    def get_screener_id(self):
        try:
            fav = self.get_fav_by_id(self.current_favid)
            return fav['screener']
        except:
            return None

    #响应favid为_id的我的收藏项的点击
    def on_nth_fav_click(self,_id):
        self.screener_listen_status = True
        self.current_favid = _id
        fav = self.find_fav_by_id(_id)
        screener_group_ctrl = self.main_ctrl.screener_group_ctrl
        #设置screener的header
        header_text = self.setting['fav_scanner_header_text']
        source_text = self.setting['fav_scanner_source_text']
        st = [header_text,fav['title'],source_text,fav['screener']]
        screener_group_ctrl.set_header(u'%s-%s %s-%s'%st)
        #设置保存按钮的text
        save_btn_text = self.setting['fav_scanner_save_button_text']
        screener_group_ctrl.set_save_btn_text(save_btn_text)
        #设置取消按钮的text
        cancel_btn_text = self.setting['fav_scanner_cancel_button_text']
        screener_group_ctrl.set_cancel_btn_text(cancel_btn_text)
        #设置main_ctrl的消息转发信号
        self.main_ctrl.set_save_transmit('save_event()')
        self.main_ctrl.set_cancel_transmit('cancel_event()')
        #向main_ctrl发送changed消息
        self.emit(QtCore.SIGNAL('changed()'))
        


