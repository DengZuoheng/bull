#!/usr/bin/python  
# -*- coding: utf-8 -*-
from PyQt4 import QtGui
from PyQt4 import Qt  
from PyQt4 import QtCore  
from view.qhoverbutton import QHoverButton
from view.qbullwindow import QBullWindow
from view.qindexlist import QIndexList
from view.qconditionwrapper import QConditionWrapper
from view.qscreenergroup import QScreenerGroup
from view.qrefreshwidget import QRefreshWidget
from view.qiconwidget import QIconWidget
from view.qfavwrapper import QFavWrapper
from controller.conditon_wrapper_ctrl import ConditionWrapperCtrl
from controller.screener_group_ctrl import ScreenerGroupCtrl
from controller.refresh_ctrl import RefreshCtrl
from controller.fav_ctrl import FavCtrl


class QMainWindow(QBullWindow):
    def __init__(self,setting,parent=None):
        kwargs = {
            'parent':parent,
            'width':setting['main_frame_width'],
            'height':setting['main_frame_height'],
            'has_close':True,
            'has_mini':True,
            'setting':setting,
        }
        super(QMainWindow,self).__init__(**kwargs)
        self.setting = setting
        self.initUI()

    def initUI(self):   
        self.init_condition_wrapper()
        self.init_fav_group()
        self.init_screener_group()
        self.init_index_list()
        self.init_refresh_group()
        self.init_icon_group()      

    def init_fav_group(self):
        setting = self.setting
        self.fav_ctrl = FavCtrl(self,setting['fav_path'])
        self.fav_wrapper = QFavWrapper(self, 
            setting['fav_wrapper_header'],
            self.fav_ctrl.fav_list, 
            setting, 
            QtGui.QImage(setting['close_icon_path']))
        self.fav_wrapper.setGeometry(*setting['condition_wrapper_geometry'])
        self.fav_wrapper.setVisible(False)
        self.connect(self.fav_wrapper,
            QtCore.SIGNAL('nth_click(int)'),
            self.on_nth_fav_click)
        self.connect(self.fav_wrapper,
            QtCore.SIGNAL('nth_close(int)'),
            self.fav_ctrl.on_nth_close)

    def init_icon_group(self):
        setting = self.setting
        icon = setting['icon_path']
        title_text = setting['title_text']
        icon_size = setting['icon_size']
        self.icon_widget = QIconWidget(self,title_text,icon,icon_size)
        self.icon_widget.setGeometry(*setting['icon_geomotry'])

    def init_refresh_group(self):
        setting = self.setting
        self.refresh_ctrl = RefreshCtrl(self)
        text = setting['refresh_text']
        gif = setting['refresh_gif']
        movie_size = setting['refresh_gif_size']
        self.refresh_widget = QRefreshWidget(self,text,gif,movie_size)
        self.refresh_widget.setGeometry(*setting['refresh_widget_geometry'])
        self.connect(self.refresh_widget,
            QtCore.SIGNAL('clicked()'),
            self.refresh_ctrl.on_refresh_start)
        self.refresh_progress_bar = QtGui.QProgressBar(self)
        self.refresh_progress_bar.setGeometry(*setting['refresh_progress_bar_geomotry'])
        #self.refresh_progress_bar.setGeometry(1,484,869,5)
        self.refresh_progress_bar.setTextVisible (False)
        self.refresh_progress_bar.setRange(0,4)
        self.refresh_progress_bar.setVisible(False)

    def init_index_list(self):
        setting=self.setting
        self.index_list = QIndexList(self,
            setting['index_list_header'],
            setting['index_list_title'],
            setting['index_list_icon'])
        self.connect(self.index_list,
            QtCore.SIGNAL('nth_btn_press(int)'),
            self.on_nth_index_press)
        self.index_list.setMaximumWidth(setting['index_list_width'])
        self.index_list.setGeometry(*setting['index_list_geometry'])

    def init_condition_wrapper(self):
        setting = self.setting
        self.condition_wrapper_ctrl = ConditionWrapperCtrl(self)
        title = setting['condition_wrapper_header']
        title_list = self.condition_wrapper_ctrl.get_title_list(setting)
        title_dict = setting['condition_wrapper_title_dict']
        self.condition_wrapper = QConditionWrapper(self,title,title_list)
        self.condition_wrapper.setGeometry(*setting['condition_wrapper_geometry'])
        self.connect(self.condition_wrapper,
            QtCore.SIGNAL('nth_changed(int,int)'),
            self.on_nth_checkbox_change)
        self.title_list = title_list

    def init_screener_group(self):
        setting = self.setting
        self.screener_group_ctrl = ScreenerGroupCtrl(self)
        init_args = self.screener_group_ctrl.get_init_args(setting)
        self.screener_group = QScreenerGroup(self,*init_args)
        self.screener_group.setGeometry(*setting['screener_group_geometry'])
        self.connect(self.screener_group,
            QtCore.SIGNAL('nth_item_close(int)'),
            self.on_nth_screener_close)
        self.connect(self.screener_group,
            QtCore.SIGNAL('submit_event()'),
            self.screener_group_ctrl.on_submit_event)
        self.connect(self.screener_group,
            QtCore.SIGNAL('cancel_event()'),
            self.screener_group_ctrl.on_cancel_event)
        self.connect(self.screener_group,
            QtCore.SIGNAL('save_event()'),
            self.screener_group_ctrl.on_save_event)

    #响应第几个条件设置项的点击. 即区分'基本指标'和'我的收藏'
    #的点击事件, 然后使相应的wrapper被响应
    def on_nth_index_press(self,_id):
        if _id == 0:
            self.condition_wrapper.setVisible(True)
            self.fav_wrapper.setVisible(False)
        else:
            self.condition_wrapper.setVisible(False)
            self.fav_wrapper.setVisible(True)

    #响应favid为_id的我的收藏项的点击
    def on_nth_fav_click(self,_id):
        fav = self.fav_ctrl.find_fav_by_id(_id)
        self.condition_wrapper.reset()
        self.screener_group.reset()
        for item in fav['condition']:
            condition_id = self.condition_wrapper_ctrl.id_map[item[0]]
            self.condition_wrapper.set_nth_state(condition_id,True)
            self.screener_group.set_nth_item_value(condition_id,item[1],item[2])
        header_text = self.setting['fav_scanner_header_text']
        self.screener_group.set_header(u'%s-%s'%(header_text,fav['title']))
        self.reset_sgbtn_connection([self.screener_group_ctrl,self.fav_ctrl])
        self.set_sgbtn_connection(self.fav_ctrl)
        save_btn_text = self.setting['fav_scanner_save_button_text']
        self.screener_group.set_save_button_text(save_btn_text)
        cancel_btn_text = self.setting['fav_scanner_cancel_button_text']
        self.screener_group.set_cancel_button_text(cancel_btn_text)
        self.fav_ctrl.current_favid = _id

    def reset_sgbtn_connection(self,ctrls):
        #这里要try, 因为不一定之前有connect
        try:
            for item in ctrls:
                self.disconnect(self.screener_group,
                    QtCore.SIGNAL('cancel_event()'),
                    item.on_cancel_event)
                self.disconnect(self.screener_group,
                    QtCore.SIGNAL('save_event()'),
                    item.on_save_event)
        except:
            pass

    def set_sgbtn_connection(self,ctrl):
        self.connect(self.screener_group,
            QtCore.SIGNAL('cancel_event()'),
            ctrl.on_cancel_event)
        self.connect(self.screener_group,
            QtCore.SIGNAL('save_event()'),
            ctrl.on_save_event)


    def on_cancel_event(self):
        pass

    def on_save_event(self):
        pass

    def on_submit_event(self):
        pass

    def on_nth_screener_close(self,id):
        self.condition_wrapper.set_nth_state(id,False)
       
    def on_nth_checkbox_change(self,state,id):
        if state == 2:
            self.screener_group.set_nth_item_visible(id,True) 
        if state == 0:
            self.screener_group.set_nth_item_visible(id,False)
      
    