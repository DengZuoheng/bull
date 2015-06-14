#!/usr/bin/python  
# -*- coding: utf-8 -*-

from PyQt4 import QtCore

class ScreenerGroupCtrl(QtCore.QObject):
    def __init__(self,screener_ctrl_list,main_ctrl):
        super(ScreenerGroupCtrl,self).__init__()
        self.screener_ctrl_list = screener_ctrl_list
        self.main_ctrl = main_ctrl
        self.screener_id = screener_ctrl_list[0].screener_id
        for item in self.screener_ctrl_list:
            self.connect(item,
                QtCore.SIGNAL('cancel_event()'),
                self.on_screener_cancel_event)
            self.connect(item,
                QtCore.SIGNAL('save_event()'),
                self.on_screener_save_event)
            self.connect(item,
                QtCore.SIGNAL('changed()'),
                self.on_screener_changed)

    def on_screener_cancel_event(self):
        self.emit(QtCore.SIGNAL('cancel_event()'))

    def on_screener_save_event(self):
        self.emit(QtCore.SIGNAL('save_event()'))

    def on_screener_changed(self):
        self.emit(QtCore.SIGNAL('changed()'))

    def get_condition(self):
        return self.get_screener_by_id(self.screener_id).get_condition()

    def set_condition(self,condition):
        screener = self.get_screener_by_id(self.screener_id)
        screener.set_condition(condition)

    def start(self):
        for item in self.screener_ctrl_list:
            if item.screener_id == self.screener_id:
                item.set_screener_visible(True)
            else:
                item.set_screener_visible(False)

    def set_screener_id(self,new_id):
        if new_id == None:
            return 
        self.screener_id = new_id
        self.start()

    def get_screener_by_id(self,screener_id):
        for item in self.screener_ctrl_list:
            if item.screener_id == self.screener_id:
                return item

    def set_header(self,header):
        screener = self.get_screener_by_id(self.screener_id)
        screener.set_header(header)

    def set_save_btn_text(self,save_btn_text):
        screener = self.get_screener_by_id(self.screener_id)
        screener.set_save_btn_text(save_btn_text)

    def set_cancel_btn_text(self,cancel_btn_text):
        screener = self.get_screener_by_id(self.screener_id)
        screener.set_cancel_btn_text(cancel_btn_text)

    def reset_button_group(self):
        screener = self.get_screener_by_id(self.screener_id)
        screener.reset_button_group()

    def reset_header(self):
        screener = self.get_screener_by_id(self.screener_id)
        screener.reset_header()

    def update_data(self):
        screener = self.get_screener_by_id(self.screener_id)
        screener.update_data()


   