#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
path = sys.path[0] 
parent_path = os.path.dirname(path) 
sys.path.insert(0,(parent_path))
import sqlite3
from sqlite_stock_dao import SqliteStockDao

class WencaiDao(SqliteStockDao):
    def __init__(self,path,table):
        super(WencaiDao,self).__init__(path,table)

    def get_parameter(self):
        parameter = [
            {'key_name':'ticker','type':'VARCHAR[20]','primary_key':True},
            {'key_name':'title','type':'VARCHAR[20]'},
            {'key_name':'change','type':'DOUBLE'},
            {'key_name':'price','type':'DOUBLE'},
            {'key_name':'pe','type':'DOUBLE'},
            {'key_name':'peg','type':'DOUBLE'},
            {'key_name':'pbv','type':'DOUBLE'},
            {'key_name':'capital','type':'DOUBLE'},
            {'key_name':'trade','type':'DOUBLE'},
            {'key_name':'business_volume','type':'DOUBLE'},
            {'key_name':'turnover','type':'DOUBLE'},
            {'key_name':'market_value','type':'DOUBLE'},
            {'key_name':'aggregate_market_value','type':'DOUBLE'},
            {'key_name':'circulation_market_value','type':'DOUBLE'},
        ]
        return parameter
        
