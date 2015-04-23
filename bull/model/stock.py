#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Stock():
    def __init__(self, 
            ticker='', 
            title='', 
            change=0, 
            price=0, 
            pe=0, 
            peg=0, 
            pbv=0, 
            capital=0, 
            trade=0):
        #股票代码
        self.ticker = ticker
        #股票简称
        self.title = title
        #涨跌幅
        self.change = change
        #现价
        self.price = price
        #市盈率
        self.pe = pe
        #动态市盈率(预测市盈率)
        self.peg = peg
        #市净率
        self.pbv = pbv
        #总股本
        self.capital = capital
        #行业
        self.trade = trade

    def __str__(self):
        ret = {
            'ticker':self.ticker,
            'title':self.title,
            'change':self.change,
            'price':self.price,
            'pe':self.pe,
            'peg':self.peg,
            'pbv':self.pbv,
            'capital':self.capital,
            'trade':self.trade,
        }
        return str(ret)
  