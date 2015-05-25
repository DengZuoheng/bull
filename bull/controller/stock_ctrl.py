#!/usr/bin/python  
# -*- coding: utf-8 -*-
import os
import sys
path = sys.path[0] 
parent_path = os.path.dirname(path) 
sys.path.insert(0,(parent_path))

from model.stock import Stock
from service.wencaispider import WencaiSpider

class StockCtrl():
    def __init__(self,stock_dao):
        self.stock_dao = stock_dao
        if stock_dao.empty():
            self.update()

    def filter(self,condition):
        result = self.stock_dao.filter(condition)
        ret = []
        for item in result:
            ret.append(Stock(*item))
        return ret

    def update(self):
        spider = WencaiSpider()
        self.stock_dao.update(spider.results())

    def update_by_result(self,result):
        self.stock_dao.update(result)

    def all(self):
        return self.filter([])