#!/usr/bin/python  
# -*- coding: utf-8 -*-
from dao.fav_dao import FavDao
class FavCtrl():
    def __init__(self,view,path='',dao=None):
        self.view = view
        if dao == None:
            self.fav_dao = FavDao(path)
        else :
            self.fav_dao = dao
        self.fav_list = self.fav_dao.load_fav()

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
        new_fav_id = self.find_max_id()
        new_fav_item = {
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
    def find_max_id(self):
        if len(self.fav_list)==0:
            return 0;
        else:
            return max([item['favid'] for item in self.fav_list])+1

    #保存当前对此收藏的改动
    def on_save_event(self):
        condition_list = self.view.screener_group_ctrl.get_condition_list()
        self.set_fav(self.current_favid,condition_list)

    #取消当前的收藏状态, 转为没有收藏的状态
    def on_cancel_event(self):
        self.view.screener_group.reset_button_group()
        self.view.screener_group.reset_header()
        self.view.reset_sgbtn_connection([self.view.screener_group_ctrl,self.view.fav_ctrl])
        self.view.set_sgbtn_connection(self.view.screener_group_ctrl)

    #响应某一个收藏被删除的信号
    def on_nth_close(self,_id):
        #这里要try, 因为一开始的时候,current_favid可能还没设置
        try:
            if _id == self.current_favid:
                self.on_cancel_event()
        except:
            pass

        self.delete_fav_by_id(_id)


