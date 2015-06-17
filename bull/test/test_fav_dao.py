#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
path = sys.path[0] 
parent_path = os.path.dirname(path) 
sys.path.insert(0,(parent_path))
import unittest
from dao.fav_dao import FavDao

class Test_test_fav_dao(unittest.TestCase):
    def test_FavDao(self):
        data = [
            {
                u"screener":"xueqiu",
                u"favid":0,
                u"title":u"我的收藏",
                u"condition":[[u"pe",0,5],[u"peg",3,200]]
            },
            {
                u"screener":"wencai",
                u"favid":1,
                u"title":u"不知道谁的收藏",
                u"condition":[[u"pe",2,6],[u"peg",20,30],[u"pbv",55,99]]
            }
        ]
        dao = FavDao('test_fav.json')
        dao.store_fav(data)
        fav = dao.load_fav()
        for i in range(len(data)):
            self.assertEqual(data[i]['screener'],fav[i]['screener'])
            self.assertEqual(data[i]['favid'],fav[i]['favid'])
            self.assertEqual(data[i]['title'],fav[i]['title'])
            self.assertEqual(len(data[i]['condition']),len(fav[i]['condition']))
            for j in range(len(data[i]['condition'])):
                self.assertEqual(data[i]['condition'][j][0],
                    fav[i]['condition'][j][0])
                self.assertEqual(data[i]['condition'][j][1],
                    fav[i]['condition'][j][1])
                self.assertEqual(data[i]['condition'][j][2],
                    fav[i]['condition'][j][2])

if __name__ == '__main__':
    unittest.main()
