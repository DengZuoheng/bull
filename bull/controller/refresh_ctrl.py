#!/usr/bin/python  
# -*- coding: utf-8 -*-
import os
import sys
path = sys.path[0] 
parent_path = os.path.dirname(path) 
sys.path.insert(0,(parent_path))
from PyQt4 import QtCore
from service.refresh_thread_factory import RefreshThreadFactory
from view.qwarning_message_box import QWarningMessageBox

class RefreshCtrl(QtCore.QObject):
    def __init__(self,view,main_ctrl,setting=None):
        super(RefreshCtrl,self).__init__()
        if setting == None:
            self.setting = view.setting
        else:
            self.setting = setting
        self.view = view
        self.main_ctrl = main_ctrl

    def on_refresh_start(self):
        self.progress = 0
        progress_bar = self.view.refresh_progress_bar
        progress_bar.setProperty('states','normal')
        progress_bar.update()
        progress_bar.style().unpolish(progress_bar)
        progress_bar.style().polish(progress_bar)
        progress_bar.setRange(0,100)
        progress_bar.setValue(0)
        progress_bar.setVisible(True)
        self.on_callback(10)
        screener_id = self.main_ctrl.get_screener_id()
        factory = RefreshThreadFactory(self.setting)
        self.refresh_thread = factory.create_refresh_thread(screener_id,self)
        self.connect(self.refresh_thread,
            QtCore.SIGNAL('finished()'),
            self.on_finish)
        self.connect(self.refresh_thread,
            QtCore.SIGNAL('callback(int)'),
            self.on_callback)
        self.connect(self.refresh_thread,
            QtCore.SIGNAL('except(const QString&)'),
            self.on_except)
        self.refresh_thread.start()

    def on_finish(self):
        if(self.refresh_thread.succeed):
            self.main_ctrl.update_data()
            self.on_callback(100)
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

    def on_callback(self,progress):
        self.view.refresh_progress_bar.setValue(progress)

    def on_except(self,err_str):
        progress_bar = self.view.refresh_progress_bar
        progress_bar.setProperty('states','danger')
        progress_bar.update()
        progress_bar.style().unpolish(progress_bar)
        progress_bar.style().polish(progress_bar)

    def update_view(self):
        print('update view')

    def except_raise(self,err):
        print(err)
        self.finish()