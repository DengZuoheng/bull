#!/usr/bin/python  
# -*- coding: utf-8 -*-
from PyQt4 import QtCore

class MainCtrl(QtCore.QObject):
    def __init__(self,main_window):
        super(MainCtrl,self).__init__()
        self.main_window = main_window
        self.screener_save_transmit = 'new_fav_event()'
        self.screener_cancel_transmit = 'reset_event()'

    def set_save_transmit(self,transmit):
        self.screener_save_transmit = transmit

    def set_cancel_transmit(self,transmit):
        self.screener_cancel_transmit = transmit

    def start(self):
        #设置第一个index_list和第一个wrapper,以及初始默认的scanner
        self.index_list_ctrl.start()
        self.wrapper_group_ctrl.start()
        self.screener_group_ctrl.start()
        #响应index_list的变化
        self.connect(self.index_list_ctrl,
            QtCore.SIGNAL('changed()'),
            self.on_index_list_change)
        #响应wrapper的变化
        self.connect(self.wrapper_group_ctrl,
            QtCore.SIGNAL('changed()'),
            self.on_wrapper_group_change)
        #响应screener的变化
        self.connect(self.screener_group_ctrl,
            QtCore.SIGNAL('changed()'),
            self.on_screener_group_change)

        #响应screener的save_btn消息
        self.connect(self.screener_group_ctrl,
            QtCore.SIGNAL('save_event()'),
            self.on_screener_group_save_event)

        #响应screener的cancel_btn消息
        self.connect(self.screener_group_ctrl,
            QtCore.SIGNAL('cancel_event()'),
            self.on_screener_group_cancel_event)
        #设置refresh组件的tooltip
        self.refresh_ctrl.setToolTip()

    def on_screener_group_save_event(self):
        self.emit(QtCore.SIGNAL(self.screener_save_transmit))

    def on_screener_group_cancel_event(self):
        temp_transmit = self.screener_cancel_transmit
        self.emit(QtCore.SIGNAL(self.screener_cancel_transmit))
        if temp_transmit == 'reset_event()':
            self.screener_group_ctrl.set_condition([])

    def on_index_list_change(self):
        #从index_list_ctrl获取要切换的wrapper_id
        wrapper_id = self.index_list_ctrl.get_current_id()
        #切换wrapper
        self.wrapper_group_ctrl.set_wrapper_id(wrapper_id)
        #再从切换后的wrapper获取screener_id
        screener_id = self.wrapper_group_ctrl.get_screener_id()
        #切换screener
        self.screener_group_ctrl.set_screener_id(screener_id)
        #设置refresh组件的tooltip
        self.refresh_ctrl.setToolTip()

    def on_screener_group_change(self):
        condition = self.screener_group_ctrl.get_condition()
        self.wrapper_group_ctrl.set_condition(condition)

    def on_wrapper_group_change(self):
        #先获取要哪个screener, 因为不用网站, 不同收藏的筛选器是不同的
        screener_id = self.wrapper_group_ctrl.get_screener_id()
        #然后设置当前screener为wrapper所需的
        self.screener_group_ctrl.set_screener_id(screener_id)
        #然后再获取condition
        condition = self.wrapper_group_ctrl.get_condition()
        #最后将condition设置到screener去
        self.screener_group_ctrl.set_condition(condition)
        #设置refresh组件的tooltip
        self.refresh_ctrl.setToolTip()

    def update_data(self):
        #更新数据完成时的操作
        self.screener_group_ctrl.update_data()

    def get_screener_id(self):
        return self.screener_group_ctrl.screener_id

    def get_condition(self):
        return self.screener_group_ctrl.get_condition()
