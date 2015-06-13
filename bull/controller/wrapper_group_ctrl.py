#!/usr/bin/python  
# -*- coding: utf-8 -*-
from PyQt4 import QtCore

class WrapperGroupCtrl(QtCore.QObject):
    def __init__(self, wrapper_ctrl_list, main_ctrl):
        super(WrapperGroupCtrl, self).__init()
        self.wrapper_ctrl_list = wrapper_ctrl_list
        self.main_ctrl = main_ctrl
        self.current_index = 0
        #响应每一个wrapper的changed消息
        for item in self.wrapper_ctrl_list:
            self.connect(item,
                QtCore.SIGNAL('changed()'),
                self.on_wrapper_changed)

    def start(self):
        self.wrapper_ctrl_list[self.current_index].set_wrapper_visible(True)
        self.wrapper_id = self.wrapper_ctrl_list[self.current_index].wrapper_id

    def set_wrapper_id(self, wrapper_id):
        self.wrapper_id = wrapper_id
        for i,ctrl in enumerate(self.wrapper_ctrl_list):
            if ctrl.wrapper_id == self.wrapper_id:
                ctrl.set_wrapper_visible(True)
                self.current_index = i
            else:
                ctrl.set_wrapper_visible(False)
        self.reset_connect()

    def get_screener_id(self):
        return self.wrapper_ctrl_list[self.current_index].get_screener_id()

    def on_wrapper_changed(self):
        #这里响应wrapper的变化信号
        pass

    def get_condition(self):
        return self.wrapper_ctrl_list[self.current_index].get_condition()

    def set_condition(self,condition):
        #每个都set_condition一下
        for item in self.connected_wrapper_ctrl_list:
            item.set_condition(condition)
        