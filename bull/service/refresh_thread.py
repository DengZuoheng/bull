#!/usr/bin/python  
# -*- coding: utf-8 -*-

import threading
import spider_factory
from PyQt4 import QtCore

class RefreshThread(QtCore.QThread):
    def __init__(self,ctrl):
        super(RefreshThread,self).__init__()
        self.ctrl = ctrl

    def run(self):
        try:
            #从工厂拿一个spider回来
            spider = spider_factory.create_spider()
            #设置spider的callback,每完成一个步骤就调用callback
            spider.set_call_back(self)
            #直接开始, 如果顺利的话就调用多次callback, 否则抛出异常
            spider.perform()
            #网络连接获取数据完成之后就存数据
            self.results = spider.results()
            #到这里就完全完成了, 如果还没有异常的话, call_back最后一次
            self.succeed = True
        except Exception as e:
            self.succeed = False
            self.emit(QtCore.SIGNAL('except(const QString&)'),unicode(e))

    #回调是用来通知进度的, 每次回调之间的操作应该都是原子的
    def call_back(self):
        self.emit(QtCore.SIGNAL('callback()'))

    def get_results(self):
        return self.results