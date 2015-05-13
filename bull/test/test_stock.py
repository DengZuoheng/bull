#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
path = sys.path[0] 
parent_path = os.path.dirname(path) 
sys.path.insert(0,(parent_path))
import unittest
from model.stock import Stock
class Test_test_stock(unittest.TestCase):
    def test_StockInit(self):
        test_data = {
            'ticker':'23333',
            'title':'ABCD',
            'change':0.123,
            'price':1.234,
            'pe':2.345,
            'peg':3.456,
            'pbv':4.567,
            'capital':5.678,
        }
        st = Stock(**test_data)
        self.assertEqual(test_data['ticker'],st.ticker)
        self.assertEqual(test_data['title'],st.title)
        self.assertEqual(test_data['change'],st.change)
        self.assertEqual(test_data['price'],st.price)
        self.assertEqual(test_data['pe'],st.pe)
        self.assertEqual(test_data['peg'],st.peg)
        self.assertEqual(test_data['pbv'],st.pbv)
        self.assertEqual(test_data['capital'],st.capital)

    def test_StockOperatorgetitem(self):
        test_data = {
            'ticker':'23333',
            'title':'ABCD',
            'change':0.123,
            'price':1.234,
            'pe':2.345,
            'peg':3.456,
            'pbv':4.567,
            'capital':5.678,
        }
        st = Stock(**test_data)
        for key in test_data:
            self.assertEqual(test_data[key],st[key])

if __name__ == '__main__':
    unittest.main()
