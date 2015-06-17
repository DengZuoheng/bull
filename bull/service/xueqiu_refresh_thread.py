#!/usr/bin/python  
# -*- coding: utf-8 -*-
#!/usr/bin/python  
# -*- coding: utf-8 -*-
import threading
from PyQt4 import QtCore
from service.xueqiu_spider import XueqiuSpider
from controller.stock_ctrl_factory import StockCtrlFactory

class XueqiuRefreshThread(QtCore.QThread):
    def __init__(self,screener_id,ctrl,setting):
        super(XueqiuRefreshThread, self).__init__()
        self.ctrl = ctrl
        self.screener_id = screener_id
        self.setting = setting
        self.progress = 2

    def run(self):
        try:
            spider = XueqiuSpider(auto_perform=False)
            stock_ctrl_factory = StockCtrlFactory(self.setting)
            stock_ctrl = stock_ctrl_factory.create_stock_ctrl('xueqiu')
            spider.set_call_back(self)
            spider.perform()
            self.results = spider.results()
            stock_ctrl.update_by_result(self.results)
            self.succeed = True
        except Exception as e:
            self.succeed = False
            self.emit(QtCore.SIGNAL('except(const QString&)'),unicode(e))


    #回调是用来通知进度的, 每次回调之间的操作应该都是原子的
    def call_back(self):
        self.progress += 2
        self.emit(QtCore.SIGNAL('callback(int)'),self.progress*10)

    def get_results(self):
        return self.results