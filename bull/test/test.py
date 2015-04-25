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

class spidertest(unittest.TestCase):
    def testWencaiSpider(self):
        spider = WencaiSpider('http://www.iwencai.com/stockpick')
        r = []
        r = spider.results()
        if(len(r)<2000):
            raise Exception('wrong total')

if __name__ =='__main__':  
    unittest.main()  