#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
path = sys.path[0] 
parent_path = os.path.dirname(path) 
sys.path.insert(0,(parent_path))
from model.stock import Stock
from service.wencaispider import WencaiSpider
from service.dataprocess import DataProcess

import unittest

class dataprocesstest(unittest.TestCase):
    def testDataProcess(self):
        sql = 'INSERT INTO      wencai(ticker,title,change,price,pe,peg,pbv,capital,trade,business_volume,turnover,market_value,aggregate_market_value,circulation_market_value)VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?)'
        spider = WencaiSpider()
        ret = spider.results()
        insert_attr = []
        for stock in ret:
            insert_attr.append(stock.attr)
        dataprocess = DataProcess()
        dataprocess.cursor.executemany(sql,insert_attr)
        dataprocess.conn.commit()
        dataprocess.execute('select * from wencai where pe < -7000')
        print dataprocess.cursor.fetchall()
if __name__ =='__main__':  
    unittest.main()  