#!/usr/bin/env python
# -*- coding: utf-8 -*-

class XueqiuStock():
    def __init__(self,**kwargs):
        for key in kwargs:
            setattr(self,key,kwargs[key])

    def __getitem__(self,key):
        return self.__dict__[key]

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
            'symbol', 'name', 'symbol', 'name', 'mc', 'fmc', 'pettm', 
            'pelyr','eps','bps', 'roediluted', 'netprofit', 'dy', 'pb', 
            'current', 'pct','pct5', 'pct10', 'pct20', 'pct1m', 'chgpct', 
            'chgpct5', 'chgpct10','chgpct20', 'chgpct1m', 'volume', 
            'volavg30', 'amount', 'tr', 'tr5', 'tr10','tr20', 'tr1m', 
            'epsdiluted', 'epsweighted', 'ocps', 'cps', 'upps', 'sps',
            'csps', 'beps', 'epsyg', 'epsqg','upqg', 'evps', 'tbi', 'bi', 
            'tbc', 'bc','bp', 'tp','np', 'pbt','tax','nbe', 'fe', 'ip', 
            'ca', 'nca', 'cl', 'ncl','tl', 'eq','teq', 'up', 'cur', 'fa', 
            'fan', 'li', 'rec', 'inv', 'ia', 'ta','cs','pc', 'fncf', 'incf', 
            'bncf', 'cnr', 'fcb', 'qr', 'cr', 'nag', 'roeweighted', 'mbig', 
            'nig', 'tag', 'sgpr', 'snpr', 'dar']