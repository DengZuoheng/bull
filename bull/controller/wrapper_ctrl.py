#!/usr/bin/python  
# -*- coding: utf-8 -*-
from PyQt4 import QtCore
from view.wrapper_factory import WrapperFactory
from controller.title_ctrl_factory import TitleCtrlFactory

class WrapperCtrl(QtCore.QObject):
    def __init__(self,wrapper_id,main_ctrl,setting):
        super(WrapperCtrl, self).__init__()
        self.wrapper_id = wrapper_id
        self.main_ctrl = main_ctrl
        self.setting = setting
        title_ctrl_factory = TitleCtrlFactory(setting)
        self.title_ctrl = title_ctrl_factory.create_title_ctrl(wrapper_id)
        wrapper_factory = WrapperFactory(setting)
        wrapper_args = [wrapper_id,main_ctrl.main_window,self.title_ctrl]
        self.wrapper = wrapper_factory.create_wrapper(*wrapper_args)
        #响应wrapper的changed消息
        self.connect(
            self.wrapper,
            QtCore.SIGNAL('changed()'),
            self.on_wrapper_changed)
        #响应main_ctrl的reset消息
        self.connect(
            self.main_ctrl,
            QtCore.SIGNAL('reset_event()'),
            self.on_reset_event)

    def on_reset_event(self):
        print('wrapper_ctrl.on_reset_event')
        self.set_condition([])

    def set_wrapper_visible(self,status):
        self.wrapper.setVisible(status)

    def on_wrapper_changed(self):
        self.emit(QtCore.SIGNAL("changed()"))

    def get_screener_id(self):
        return self.wrapper_id

    def get_condition(self):
        return self.wrapper.get_condition()

    def set_condition(self,condition):
        self.wrapper.set_condition(condition)