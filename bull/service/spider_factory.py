#!/usr/bin/python  
# -*- coding: utf-8 -*-
from wencai_spider import WencaiSpider
from xueqiu_spider import XueqiuSpider

class SpiderFactory():
    def __init__(self,setting):
        self.setting = setting

    def create_spider(self, stock_type):
        setting = self.setting
        if stock_type == 'wencai':
            spider = WencaiSpider()
        elif stock_type == 'xueqiu':
            spider = XueqiuSpider()
        return spider