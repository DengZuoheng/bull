#!/usr/bin/python  
# -*- coding: utf-8 -*-
import os
import sys
path = sys.path[0] 
parent_path = os.path.dirname(path) 
sys.path.insert(0,(parent_path))
from service.spider_factory import SpiderFactory

class StockCtrl():
    def __init__(self,setting,stock_dao,stock_cls,stock_type):
        self.setting = setting
        self.stock_type = stock_type
        self.stock_dao = stock_dao
        self.stock_cls = stock_cls
        if stock_dao.empty():
            self.update()

    def filter(self,condition):
        result = self.stock_dao.filter(condition)
        ret = []
        for item in result:
            ret.append(self.stock_cls(*item))
        return ret

    def update_by_result(self,result):
        self.stock_dao.update(result)

    def all(self):
        return self.filter([])

    def empty(self):
        return len(self.all())<=0

    def update(self):
        spider_factory = SpiderFactory(self.setting)
        spider = spider_factory.create_spider(self.stock_type)
        #spider.perform() #auto perform is default
        ret = spider.results()
        self.update_by_result(ret)

    def get_data_list(self,title_ctrl):
        all_stock = self.all()
        title_dict = title_ctrl.get_indicator_dict()
        length = len(title_dict)
        ret = []
        for key in title_dict:
            ret.append({'data':[],'data_max':None,'data_min':None})
        for item in all_stock:
            i = 0
            for indicator in title_dict:
                key = indicator.replace('%s_'%title_ctrl.get_prefix(),'')           
                if item[key] is not None:
                    ret[i]['data'].append(item[key]) 
                    if ret[i]['data_max'] is None:
                        ret[i]['data_max'] = item[key]
                    elif ret[i]['data_max'] < item[key]:
                        ret[i]['data_max'] = item[key]
                    if ret[i]['data_min'] is None:
                        ret[i]['data_min'] = item[key]
                    elif ret[i]['data_min'] >item[key]:
                        ret[i]['data_min'] = item[key]
                i = i+1
        return ret