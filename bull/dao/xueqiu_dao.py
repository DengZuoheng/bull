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
            #列名和类型, 具体可参考wencai_dao.py
        ]
        return parameter
        
