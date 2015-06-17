#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
path = sys.path[0] 
parent_path = os.path.dirname(path) 
sys.path.insert(0,(parent_path))

from service.spider import Spider
from service.wencai_spider import WencaiSpider
from model.wencai_stock import WencaiStock
import unittest

class Test_test_WencaiSpider(unittest.TestCase):
    def test_WencaiSpider(self):
        spider = WencaiSpider('http://www.iwencai.com/stockpick',auto_perform=False)
        spider.perform()
        r = []
        r = spider.results()
        self.assertGreater(len(r),2000)
        if not isinstance(r[0],WencaiStock):
            raise Exception('type error: result item is not Stock instance')

if __name__ == '__main__':
    unittest.main()
