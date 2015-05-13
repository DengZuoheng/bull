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

class Test_test_wencaidao(unittest.TestCase):
    def test_Constructor(self):
        dao = WencaiDao('../db.sqlite3')

    def test_Update(self):
        spider = WencaiSpider()
        ret = spider.results()
        dao = WencaiDao('../db.sqlite3')
        dao.update(ret)
        self.assertEqual(len(ret),len(dao.all()))

    def test_Filter(self):
        dao = WencaiDao('../db.sqlite3')
        cond = [('pe',0,5)]
        ret = dao.filter(cond)
        self.assertGreater(len(ret),1)
        stock = Stock(*ret[0])
        self.assertGreater(stock.pe,0)
        self.assertGreater(5,stock.pe)

if __name__ == '__main__':
    unittest.main()
