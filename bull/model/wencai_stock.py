#!/usr/bin/env python
# -*- coding: utf-8 -*-
from stock import Stock
class WencaiStock(Stock):
    def __init__(self, 
            ticker='', 
            title='', 
            change=0, 
            price=0, 
            pe=0, 
            peg=0, 
            pbv=0, 
            capital=0, 
            trade=None,
            business_volume=None,
            turnover=None,
            market_value=None,
            aggregate_market_value=None,
            circulation_market_value=None
            ):
        super(WencaiStock,self).__init__()
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
        #成交价
        self.business_volume = business_volume
        #成交额
        self.turnover = turnover
        #总市值
        self.market_value=market_value
        #总市值
        self.aggregate_market_value = aggregate_market_value
        #流通市值
        self.circulation_market_value = circulation_market_value
        
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
            'business_volume':self.business_volume,
            'turn_over':self.turnover,
            'market_value':self.market_value,
            'aggregate_market_value':self.aggregate_market_value,
            'circulation_market_value':self.circulation_market_value
        }
        return str(ret)

    def get_type_by_key(self,key):
        if self[key] == None:
            return 'null'
        elif key=='ticker' or key=='title':
            return 'str'
        else:
            return 'double'
  