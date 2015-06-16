#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
path = sys.path[0] 
parent_path = os.path.dirname(path) 
sys.path.insert(0,(parent_path))
import sqlite3
from stock_dao import StockDao

class SqliteStockDao(StockDao):
    def __init__(self,path,table):
        super(SqliteStockDao,self).__init__()
        self.path = path
        self.table = table
        try:
            self.conn=sqlite3.connect(self.path)
            self.cursor=self.conn.cursor()
            self.cursor.execute(self.__gen_sql())
        except sqlite3.Erroe as e:
            raise Excepiton('db connect error')

    #按条件查找
    def filter(self,condition):
        cond = condition
        if len(cond)!=0:
            sql = 'SELECT * FROM %s WHERE '%self.table
            for i in range(len(cond )):
                str_sql = '( %s BETWEEN %f AND %f )'%cond[i]
                if(i!=len(cond)-1):
                    str_sql = str_sql + ' AND '
                sql = sql + str_sql
        else:
            sql = 'SELECT * FROM %s'%self.table
        self.cursor.execute(sql)
        ret = self.cursor.fetchall()
        #返回的是一堆元组
        return ret

    #更新所有数据_
    def update(self,stocks):
        self.conn.execute('DELETE FROM %s'%self.table)
        attrs = self.get_attrs()
        #根据上面的属性列表构造一个insert语句
        t = (self.table, '%s, '*(len(attrs)-1), '%s', '?,'*(len(attrs)-1))
        str_sql = 'INSERT INTO %s(%s%s)VALUES(%s?)'%t
        sql = str_sql%tuple(attrs)
        insert_attr = []
        for item in stocks:
            sub_attr = []
            for key in attrs:
                sub_attr.append(getattr(item,key))
            insert_attr.append(tuple(sub_attr))

        self.cursor.executemany(sql, insert_attr)
        self.conn.commit()

    #获取所有结果, 没什么用, 就是测试用的
    def get_attrs(self):
        parameter = self.get_parameter()
        return [item['key_name'] for item in parameter]

    def all(self):
        return self.filter([])

    def empty(self):
        return len(self.all()) == 0

    def __gen_sql(self):
        parameter = self.get_parameter()
        sql = 'CREATE TABLE IF NOT EXISTS %s ('%self.table
        for i in range(len(parameter)):
            _str = '%s %s'%(parameter[i]['key_name'],parameter[i]['type'])
            if 'primary_key' in parameter[i]:
                _str = _str + ' %s'%'PRIMARY_KEY'
            if(i != len(parameter) - 1):
                _str = _str +','
            else:
                _str = _str +')'
            sql = sql + _str
        return sql

    def get_parameter(self):
        pass