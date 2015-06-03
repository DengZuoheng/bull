#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
path = sys.path[0] 
parent_path = os.path.dirname(path) 
sys.path.insert(0,(parent_path))
import unittest
from dao.title_dao import TitleDao
from service.wencaispider import WencaiSpider

class Test_test_title_dao(unittest.TestCase):
    def test_LoadTitle(self):
        dao = TitleDao()
        spider = WencaiSpider()
        titles = spider.titles()
        dao.store_title(titles)
        titles = dao.load_title()
        self.assertEqual(len(titles),9)
        for item in titles:
            print(item)
            if not isinstance(item,unicode):
                raise Exception('title item is not a string')


    def test_StoreTitle(self):
        dao = TitleDao()
        spider = WencaiSpider()
        titles = spider.titles()
        dao.store_title(titles)

if __name__ == '__main__':
    unittest.main()