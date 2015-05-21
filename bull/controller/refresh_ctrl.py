#!/usr/bin/python  
# -*- coding: utf-8 -*-
import os
import sys
path = sys.path[0] 
parent_path = os.path.dirname(path) 
sys.path.insert(0,(parent_path))
from PyQt4 import QtCore
from service.refresh_thread import RefreshThread

class RefreshCtrl(QtCore.QObject):
    def __init__(self,view,setting=None):
        super(RefreshCtrl,self).__init__()
        if setting == None:
            self.setting = view.setting
        else:
            self.setting = setting
        self.view = view

    def on_refresh_start(self):
        self.refresh_thread = RefreshThread(self)
        self.connect(self.refresh_thread,
            QtCore.SIGNAL('finished()'),
            self.on_finish)
        self.connect(self.refresh_thread,
            QtCore.SIGNAL('callback()'),
            self.on_callback)
        self.connect(self.refresh_thread,
            QtCore.SIGNAL('except(const QString&)'),
            self.on_except)
        self.refresh_thread.start()

    def on_finish(self):
        if(self.refresh_thread.succeed):
            stock_ctrl = self.get_stock_ctrl()
            stock_ctrl.update_by_result(self.refresh_thread.get_results())
            self.view.screener_group_ctrl.update_data()
        print('update')
        self.view.refresh_widget.set_clickable(True)
        self.view.refresh_widget.set_movie_paused_status(True)

    def on_callback(self):
        print('call_back')
        
    def get_stock_ctrl(self):
        return self.view.screener_group_ctrl.stock_ctrl

    def on_except(self,err_str):
        print(err_str)

    def update_view(self):
        print('update view')

    def except_raise(self,err):
        print(err)
        self.finish()