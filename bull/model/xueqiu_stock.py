#!/usr/bin/env python
# -*- coding: utf-8 -*-
from stock import Stock

class XueqiuStock(Stock):
    def __init__(self, *args, **kwargs):
        super(XueqiuStock, self).__init__()
        if args:
            self.symbol = args[0]
            self.name = args[1]
            i = 2
            for key in self.attr_list():
                setattr(self,key,args[i])
                i = i+1
        if kwargs:
            for key in kwargs:
                setattr(self,key,kwargs[key])

    def get_type_by_key(self,key):
        if self[key] == None:
            return 'null'
        elif key=='symbol' or key=='name':
            return 'str'
        else:
            return 'double'

    @classmethod
    def attr_list(cls):
        return [
            "pct1m", "pelyr", "chgpct", "tr1m", "tr20", "pb" , "chgpct1m", 
            "pct20", "tr", "pct", "current", "pettm", "chgpct20", "tr5", "fmc", 
            "chgpct5", "tr10", "evps", "volavg30", "volume", "pct10", "dy", 
            "mc", "amount", "pct5", "chgpct10"]