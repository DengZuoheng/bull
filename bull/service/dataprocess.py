#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import sqlite3
path = sys.path[0] 
parent_path = os.path.dirname(path) 
sys.path.insert(0,(parent_path))
DB_SQLITE_PATH="../db_wencai.sqlite3"
class DataProcess():
    def __init__(self):
        
        try:
            print parent_path
            self.conn=sqlite3.connect(DB_SQLITE_PATH)
            self.cursor=self.conn.cursor()
            self.cursor.execute(self.gen_sql())
        except sqlite3.Error,e:
            print "连接sqlite3数据库失败", ":", e.args[0]
        
    def execute(self,sql):
        try:
            self.cursor.execute(sql)
        except sqlite3.Error,e:
            print "语句执行出错",":",e.args[0]
        
    def getresult(self):
        return self.cursor.fetchall()
        
    def gen_sql(self):
        parameter = []
        sql = 'create table if not exists wencai ('
        
        ticker = 'ticker VARCHAR[20] primary key'
        parameter.append(ticker)
        
        title = 'title VARCHAR[20]'
        parameter.append(title)
        
        change = 'change REAL'
        parameter.append(change)
        
        price = 'price DOUBLE'
        parameter.append(price)
        
        pe = 'pe DOUBLE'
        parameter.append(pe)
        
        peg = 'peg DOUBLE'
        parameter.append(peg)
        
        pbv = 'pbv DOUBLE'
        parameter.append(pbv)
        
        capital = 'capital DOUBLE'
        parameter.append(capital)
        
        trade = 'trade DOUBLE'
        parameter.append(trade)
        
        business_volume = 'business_volume DOUBLE'
        parameter.append(business_volume)
        
        turnover = 'turnover DOUBLE'
        parameter.append(turnover)
        
        market_value = 'market_value DOUBLE'
        parameter.append(market_value)
        
        aggregate_market_value = 'aggregate_market_value DOUBLE'
        parameter.append(aggregate_market_value)
        
        circulation_market_value = 'circulation_market_value DOUBLE'
        parameter.append(circulation_market_value)

        for i in range(0,len(parameter)):
            sql = sql + parameter[i]
            if(i != len(parameter) - 1):
                sql = sql + ','
            else:
                sql = sql + ')'
        return sql