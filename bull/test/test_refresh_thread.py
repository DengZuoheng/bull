#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
path = sys.path[0]
parent_path = os.path.dirname(path)
sys.path.insert(0,(parent_path))
import unittest
from PyQt4 import QtCore
from service.wencai_refresh_thread import WencaiRefreshThread
from service.xueqiu_refresh_thread import XueqiuRefreshThread
from model.wencai_stock import WencaiStock
from model.xueqiu_stock import XueqiuStock
from controller.setting_ctrl import SettingCtrl

#一个ctrl的mockup, 仅用于测试
class CtrlMockup(QtCore.QObject):
    def __init__(self):
        super(CtrlMockup,self).__init__()
        self.call_back_count=0
        self.except_count = 0

    def on_except(self,qstr):
        self.except_count += 1
    
    def on_call_back(self,count):
        self.call_back_count += 1

class Test_test_refresh_thread(unittest.TestCase):
    def test_WencaiRefreshThread(self):
        setting_ctrl = SettingCtrl()
        ctrl = CtrlMockup()
        thread = WencaiRefreshThread('wencai',ctrl,setting_ctrl.get_setting())
        #绑定线程对象的回调信号
        a = ctrl.connect(thread,QtCore.SIGNAL('callback(int)'),ctrl.on_call_back)
        self.assertEqual(a,True)
        #绑定线程的失败信号
        b = ctrl.connect(thread,QtCore.SIGNAL('except(const QString&)'),ctrl.on_except)
        self.assertEqual(b,True)
        thread.start()
        thread.wait()
        if thread.succeed:
            ret = thread.get_results()
            #返回数量应该大于两千
            self.assertGreater(len(ret),1000)
            for item in ret:
                #返回列表每一个都应该是Stock的实例
                self.assertIsInstance(item,WencaiStock)
        else:
            raise Exception('failed')

    def test_XueqiuRefreshThread(self):
        setting_ctrl = SettingCtrl()
        ctrl = CtrlMockup()
        thread = XueqiuRefreshThread('xueqiu',ctrl,setting_ctrl.get_setting())
        #绑定线程对象的回调信号
        a = ctrl.connect(thread,QtCore.SIGNAL('callback(int)'),ctrl.on_call_back)
        self.assertEqual(a,True)
        #绑定线程的失败信号
        b = ctrl.connect(thread,QtCore.SIGNAL('except(const QString&)'),ctrl.on_except)
        self.assertEqual(b,True)
        thread.start()
        thread.wait()
        if thread.succeed:
            ret = thread.get_results()
            #返回数量应该大于两千
            self.assertGreater(len(ret),1000)
            for item in ret:
                #返回列表每一个都应该是Stock的实例
                self.assertIsInstance(item,XueqiuStock)
        else:
            raise Exception('failed')

if __name__ == '__main__':
    unittest.main()
