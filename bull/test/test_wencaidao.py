#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
path = sys.path[0] 
parent_path = os.path.dirname(path) 
sys.path.insert(0,(parent_path))
import unittest
from dao.wencai_dao import WencaiDao
from model.stock import Stock
from service.wencaispider import WencaiSpider

#测试问财的数据访问对象
class Test_test_wencaidao(unittest.TestCase):
    #测试构造函数(废话)
    def test_Constructor(self):
        dao = WencaiDao('../db.sqlite3')

    #测试更新数据库
    def test_WencaiDao_Update(self):
        spider = WencaiSpider()
        ret = spider.results()
        dao = WencaiDao('../db.sqlite3')
        dao.update(ret)
        self.assertEqual(len(ret),len(dao.all()))
    #测试"按单个条件检索"
    def test_WencaiDao_Filter(self):
        dao = WencaiDao('../db.sqlite3')
        cond = [('pe',0,10)]
        ret = dao.filter(cond)
        self.assertGreater(len(ret),1)
        stock = Stock(*ret[0])
        self.assertGreater(stock.pe,0)
        self.assertGreater(10,stock.pe)
    #测试"按多个条件检索"
    def test_WencaiDao_Filter_Multi(self):
        dao = WencaiDao('../db.sqlite3')
        cond = [('pe',-7000,7000),('peg',-1000,1000)]
        ret = dao.filter(cond)
        self.assertGreater(len(ret),1)
        for item in ret:
            stock = Stock(*item)
            self.assertGreater(stock['pe'],-7000)
            self.assertGreater(7000,stock['pe'])
            self.assertGreater(stock['peg'],-1000)
            self.assertGreater(1000,stock['peg'])

if __name__ == '__main__':
    unittest.main()
