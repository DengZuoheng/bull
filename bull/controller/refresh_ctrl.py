#!/usr/bin/python  
# -*- coding: utf-8 -*-
import os
import sys
path = sys.path[0] 
parent_path = os.path.dirname(path) 
sys.path.insert(0,(parent_path))
from PyQt4 import QtCore
from service.refresh_thread import RefreshThread
from view.qwarningmessagebox import QWarningMessageBox

class RefreshCtrl(QtCore.QObject):
    def __init__(self,view,setting=None):
        super(RefreshCtrl,self).__init__()
        if setting == None:
            self.setting = view.setting
        else:
            self.setting = setting
        self.view = view
        self.progress = 0

    def on_refresh_start(self):
        self.progress = 0
        self.view.refresh_progress_bar.setProperty('states','normal')
        self.view.refresh_progress_bar.update()
        self.view.refresh_progress_bar.style().unpolish(self.view.refresh_progress_bar)
        self.view.refresh_progress_bar.style().polish(self.view.refresh_progress_bar)
        self.view.refresh_progress_bar.setRange(0,4)
        self.view.refresh_progress_bar.setValue(0)
        self.view.refresh_progress_bar.setVisible(True)
        self.on_callback()
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
            self.on_callback()
            self.view.refresh_widget.set_clickable(True)
            self.view.refresh_widget.set_movie_paused_status(True)
            self.view.refresh_progress_bar.setVisible(False)
        else:
            try:     
                data = {
                    'setting':self.setting,
                    'warning_text':self.setting['refresh_error_text']
                }
                #这个消息框得传一个data字典, 包括setting和警告字符串
                messagebox = QWarningMessageBox(self.view,data)
                messagebox.exec_()
            except Exception as e:
                print(str(e))
            self.view.refresh_widget.set_clickable(True)
            self.view.refresh_widget.set_movie_paused_status(True)
            self.view.refresh_progress_bar.setVisible(False)

    def on_callback(self):
        self.progress += 1
        self.view.refresh_progress_bar.setValue(self.progress)
        
    def get_stock_ctrl(self):
        return self.view.screener_group_ctrl.stock_ctrl

    def on_except(self,err_str):
        self.view.refresh_progress_bar.setProperty('states','danger')
        self.view.refresh_progress_bar.update()
        self.view.refresh_progress_bar.style().unpolish(self.view.refresh_progress_bar)
        self.view.refresh_progress_bar.style().polish(self.view.refresh_progress_bar)
        


    def update_view(self):
        print('update view')

    def except_raise(self,err):
        print(err)
        self.finish()