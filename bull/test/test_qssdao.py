#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
path = sys.path[0] 
parent_path = os.path.dirname(path) 
sys.path.insert(0,(parent_path))
import unittest

from dao.qss_dao import QSSDao

class Test_test_qssdao(unittest.TestCase):
    def test_QssDao(self):
        qss = """
            *{
                border: 1px solid #fff;
            }
        """
        dao = QSSDao('qss.qss')
        dao.store_qss(qss)
        dao2 = QSSDao('qss.qss')
        s = dao2.load_qss()
        self.assertGreater(len(s),1)

if __name__ == '__main__':
    unittest.main()
