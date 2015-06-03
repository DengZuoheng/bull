#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
path = sys.path[0]
parent_path = os.path.dirname(path)
sys.path.insert(0,(parent_path))
import unittest
from PyQt4 import QtCore
from service.refresh_thread import RefreshThread
from model.stock import Stock

#一个ctrl的mockup, 仅用于测试
class CtrlMockup(QtCore.QObject):
    def __init__(self):
        super(CtrlMockup,self).__init__()
        self.call_back_count=0
        self.except_count = 0

    def on_except(self,qstr):
        self.except_count += 1
    
    def on_call_back(self):
        print("JJJ")
        self.call_back_count += 1

class Test_test_refresh_thread(unittest.TestCase):
    def test_RefreshThread(self):
        ctrl = CtrlMockup()
        thread = RefreshThread(ctrl)
        #绑定线程对象的回调信号
        ctrl.connect(thread,QtCore.SIGNAL('callback()'),ctrl.on_call_back)
        #绑定线程的失败信号
        ctrl.connect(thread,QtCore.SIGNAL('except(const QString&)'),ctrl.on_except)
        thread.start()
        thread.wait()
        if thread.succeed:
            ret = thread.get_results()
            #返回数量应该大于两千
            self.assertGreater(len(ret),2000)
            for item in ret:
                #返回列表每一个都应该是Stock的实例
                self.assertIsInstance(item,Stock)



if __name__ == '__main__':
    unittest.main()
