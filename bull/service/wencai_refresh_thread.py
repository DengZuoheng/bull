#!/usr/bin/python  
# -*- coding: utf-8 -*-
import threading
from PyQt4 import QtCore
from service.wencai_spider import WencaiSpider
from controller.stock_ctrl_factory import StockCtrlFactory

class WencaiRefreshThread(QtCore.QThread):
    def __init__(self,screener_id,ctrl,setting):
        super(WencaiRefreshThread,self).__init__()
        self.ctrl = ctrl
        self.screener_id = screener_id
        self.setting = setting
        self.progress = 2

    def run(self):
        try:
            spider = WencaiSpider(auto_perform=False)
            stock_ctrl_factory = StockCtrlFactory(self.setting)
            stock_ctrl = stock_ctrl_factory.create_stock_ctrl('wencai')
            #设置spider的callback,每完成一个步骤就调用callback
            spider.set_call_back(self)
            #直接开始, 如果顺利的话就调用多次callback, 否则抛出异常
            spider.perform()
            #网络连接获取数据完成之后就存数据
            self.results = spider.results()
            stock_ctrl.update_by_result(self.results)

            #到这里就完全完成了, 如果还没有异常的话, call_back最后一次
            self.succeed = True
        except Exception as e:
            self.succeed = False
            self.emit(QtCore.SIGNAL('except(const QString&)'),unicode(e))

    #回调是用来通知进度的, 每次回调之间的操作应该都是原子的
    def call_back(self):
        self.progress += 1
        self.emit(QtCore.SIGNAL('callback(int)'),self.progress*10)

    def get_results(self):
        return self.results