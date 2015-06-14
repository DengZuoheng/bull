#!/usr/bin/python  
# -*- coding: utf-8 -*-
#!/usr/bin/python  
# -*- coding: utf-8 -*-
import threading
from PyQt4 import QtCore

class XueqiuRefreshThread(QtCore.QThread):
    def __init__(self,screener_id,ctrl,setting):
        super(XueqiuRefreshThread, self).__init__()
        self.ctrl = ctrl
        self.screener_id = screener_id
        self.setting = setting

    def run(self):
        #TODO
        pass

    #回调是用来通知进度的, 每次回调之间的操作应该都是原子的
    def call_back(self):
        self.emit(QtCore.SIGNAL('callback()'))

    def get_results(self):
        return self.results