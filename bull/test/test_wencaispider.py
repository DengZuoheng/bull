#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
path = sys.path[0] 
parent_path = os.path.dirname(path) 
sys.path.insert(0,(parent_path))

from service.spider import Spider
from service.wencaispider import WencaiSpider
import unittest

class Test_test_wencaispider(unittest.TestCase):
    def test_WencaiSpider(self):
        spider = WencaiSpider('http://www.iwencai.com/stockpick')
        r = []
        r = spider.results()
        self.assertGreater(len(r),2000)

if __name__ == '__main__':
    unittest.main()
