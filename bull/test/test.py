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
        item = []
        item = spider.results()
        if(len(item)<2000):
            raise Excetion('wrong total')
        """
        for item in self.save:
            print(item)
        """

if __name__ =='__main__':  
    unittest.main()  