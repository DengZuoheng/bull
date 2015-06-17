#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
path = sys.path[0] 
parent_path = os.path.dirname(path) 
sys.path.insert(0,(parent_path))
import unittest
from model.wencai_stock import WencaiStock
from model.xueqiu_stock import XueqiuStock

class Test_test_stock(unittest.TestCase):
    def test_WencaiStock(self):
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
        st = WencaiStock(**test_data)
        self.assertEqual(test_data['ticker'],st.ticker)
        self.assertEqual('str',st.get_type_by_key('ticker'))
        self.assertEqual(test_data['title'],st.title)
        self.assertEqual('str',st.get_type_by_key('title'))
        self.assertEqual(test_data['change'],st.change)
        self.assertEqual('double',st.get_type_by_key('price'))
        self.assertEqual(test_data['price'],st.price)
        self.assertEqual('double',st.get_type_by_key('pe'))
        self.assertEqual(test_data['pe'],st.pe)
        self.assertEqual('double',st.get_type_by_key('peg'))
        self.assertEqual(test_data['peg'],st.peg)
        self.assertEqual('double',st.get_type_by_key('pbv'))
        self.assertEqual(test_data['pbv'],st.pbv)
        self.assertEqual('double',st.get_type_by_key('capital'))
        self.assertEqual(test_data['capital'],st.capital) 
        self.assertEqual('double',st.get_type_by_key('change'))
        for key in test_data:
            self.assertEqual(test_data[key],st[key])  

    def test_XueqiuStock(self):
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
        st = XueqiuStock(**test_data)
        for key in test_data:
            self.assertEqual(test_data[key],st[key]) 
            self.assertEqual('double',st.get_type_by_key(key))
        ret = XueqiuStock.attr_list()
        self.assertEqual([
            "pct1m", "pelyr", "chgpct", "tr1m", "tr20", "pb" , "chgpct1m", 
            "pct20", "tr", "pct", "current", "pettm", "chgpct20", "tr5", "fmc", 
            "chgpct5", "tr10", "evps", "volavg30", "volume", "pct10", "dy", 
            "mc", "amount", "pct5", "chgpct10"], ret)

    

if __name__ == '__main__':
    unittest.main()
