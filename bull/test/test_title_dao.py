#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
path = sys.path[0] 
parent_path = os.path.dirname(path) 
sys.path.insert(0,(parent_path))
import unittest
from dao.title_dao import TitleDao

class Test_test_title_dao(unittest.TestCase):
    def test_TitleDao(self):
        dao = TitleDao('wencai_title.json')
        dao.load_title()
        titles = dao.load_title()
        assert(titles.has_key('prefix'))
        assert(titles.has_key('title'))
        assert(titles.has_key('indicator'))
        assert(titles.has_key('header'))
        assert(isinstance(titles['prefix'],unicode))
        assert(isinstance(titles['title'],dict))
        assert(isinstance(titles['indicator'],list))
        assert(isinstance(titles['header'],list))


if __name__ == '__main__':
    unittest.main()