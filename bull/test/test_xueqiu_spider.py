#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
path = sys.path[0] 
parent_path = os.path.dirname(path) 
sys.path.insert(0,(parent_path))

from service.spider import Spider
from service.xueqiu_spider import XueqiuSpider
from model.xueqiu_stock import XueqiuStock
from dao.xueqiu_dao import XueqiuDao
import unittest

class Test_test_xueqiuspider(unittest.TestCase):
    def test_XueqiuSpider(self):
        spider = XueqiuSpider()
        r = []
        r = spider.results()
        self.assertGreater(len(r),1000)
        if not isinstance(r[0],XueqiuStock):
            raise Exception('type error: result item is not Stock instance')
        dao = XueqiuDao('db.sqlite3','xueqiu')
        dao.update(r)

if __name__ == '__main__':
    unittest.main()
