#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
path = sys.path[0] 
parent_path = os.path.dirname(path) 
sys.path.insert(0,(parent_path))
import sqlite3
from sqlite_stock_dao import SqliteStockDao

class XueqiuDao(SqliteStockDao):
    def __init__(self,path,table):
        super(XueqiuDao,self).__init__(path,table)

    def get_parameter(self):
        parameter = [
            {'key_name':'symbol','type':'VARCHAR[20]','primary_key':True},
            {'key_name':'name','type':'VARCHAR[20]'},
            {'key_name':'pct1m','type':'DOUBLE'},
            {'key_name':'pelyr','type':'DOUBLE'},
            {'key_name':'chgpct','type':'DOUBLE'},
            {'key_name':'tr1m','type':'DOUBLE'},
            {'key_name':'tr20','type':'DOUBLE'},
            {'key_name':'pb','type':'DOUBLE'},
            {'key_name':'chgpct1m','type':'DOUBLE'},
            {'key_name':'pct20','type':'DOUBLE'},
            {'key_name':'tr','type':'DOUBLE'},
            {'key_name':'pct','type':'DOUBLE'},
            {'key_name':'current','type':'DOUBLE'},
            {'key_name':'pettm','type':'DOUBLE'},
            {'key_name':'chgpct20','type':'DOUBLE'},
            {'key_name':'tr5','type':'DOUBLE'},
            {'key_name':'fmc','type':'DOUBLE'},
            {'key_name':'chgpct5','type':'DOUBLE'},
            {'key_name':'tr10','type':'DOUBLE'},
            {'key_name':'evps','type':'DOUBLE'},
            {'key_name':'volavg30','type':'DOUBLE'},
            {'key_name':'volume','type':'DOUBLE'},
            {'key_name':'pct10','type':'DOUBLE'},
            {'key_name':'dy','type':'DOUBLE'},
            {'key_name':'mc','type':'DOUBLE'},
            {'key_name':'amount','type':'DOUBLE'},
            {'key_name':'pct5','type':'DOUBLE'},
            {'key_name':'chgpct10','type':'DOUBLE'},
        ]
        return parameter
        
