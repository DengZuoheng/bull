#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
path = sys.path[0] 
parent_path = os.path.dirname(path) 
sys.path.insert(0,(parent_path))
import unittest
from dao.xueqiu_dao import XueqiuDao
from model.xueqiu_stock import XueqiuStock
from service.xueqiu_spider import XueqiuSpider

class Test_test_xueqiu_dao(unittest.TestCase):
    #测试更新
    def test_XueqiuDao_Update(self):
        spider = XueqiuSpider()
        ret = spider.results()
        dao = XueqiuDao('../db.sqlite3','xueqiu')
        dao.update(ret)
        self.assertEqual(len(ret),len(dao.all()))

     #测试"按单个条件检索"
    def test_XueqiuDao_Filter(self):
        dao = XueqiuDao('../db.sqlite3','xueqiu')
        cond = [('mc',0,10000)]
        ret = dao.filter(cond)
        self.assertGreater(len(ret),1)
        stock = XueqiuStock(*ret[0])
        self.assertGreater(stock.mc,0)
        self.assertGreater(10000,stock.mc)

    #测试"按多个条件检索"
    def test_XueqiuDao_Filter_Multi(self):
        dao = XueqiuDao('../db.sqlite3','xueqiu')
        cond = [('mc',-7000,7000),('fmc',-10000,10000)]
        ret = dao.filter(cond)
        self.assertGreater(len(ret),1)
        for item in ret:
            stock = XueqiuStock(*item)
            self.assertGreater(stock['mc'],-7000)
            self.assertGreater(7000,stock['mc'])
            self.assertGreater(stock['fmc'],-10000)
            self.assertGreater(10000,stock['fmc'])

if __name__ == '__main__':
    unittest.main()
