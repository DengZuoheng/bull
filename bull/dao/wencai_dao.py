#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
path = sys.path[0] 
parent_path = os.path.dirname(path) 
sys.path.insert(0,(parent_path))
import sqlite3
from stock_dao import StockDao

class WencaiDao(StockDao):
    def __init__(self,path):
        super(WencaiDao,self).__init__()
        self.path = path
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
            sql = 'SELECT * FROM wencai WHERE '
            for i in range(len(cond )):
                t= (cond[i][0],cond[i][1],cond[i][2])
                str_sql = '( %s BETWEEN %f AND %f )'%t
                if(i!=len(cond)-1):
                    str_sql = str_sql + ' AND '
                sql = sql + str_sql
        else:
            sql = 'select * from wencai'
        self.cursor.execute(sql)
        ret = self.cursor.fetchall()
        #返回的是一堆元组
        return ret

    #更新所有数据
    def update(self,stocks):
        self.conn.execute('delete from wencai')
        attrs = [
            'ticker',
            'title',
            'change',
            'price',
            'pe',
            'peg',
            'pbv',
            'capital',
            'trade',
            'business_volume',
            'turnover',
            'market_value',
            'aggregate_market_value',
            'circulation_market_value'
        ]
        #根据上面的属性列表构造一个insert语句
        t = ('%s,'*(len(attrs)-1),'%s','?,'*(len(attrs)-1))
        str_sql = 'INSERT INTO wencai(%s%s)VALUES(%s?)'%t
        sql = str_sql%tuple(attrs)

        insert_attr = []
        for item in stocks:
            insert_attr.append(item.attr)
        self.cursor.executemany(sql, insert_attr)
        self.conn.commit()

    #获取所有结果, 没什么用, 就是测试用的
    def all(self):
        return self.filter([])

    def __gen_sql(self):
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
        sql = 'CREATE TABLE IF NOT EXISTS WENCAI ('

        for i in range(len(parameter)):
            str = '%s %s'%(parameter[i]['key_name'],parameter[i]['type'])
            if 'primary_key' in parameter[i]:
                str = str + ' %s'%'PRIMARY_KEY'
            if(i != len(parameter) - 1):
                str = str +','
            else:
                str = str +')'
            sql = sql + str
        return sql
