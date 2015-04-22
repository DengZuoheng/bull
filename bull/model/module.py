#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Module():
    def __init__(self,cursor):
        self.code = cursor[0]
        self.name = cursor[1]
        self.increase = cursor[2]
        self.price = cursor[3]
        self.pe = cursor[4]
        self.forcast = cursor[5]
        self.pbv = cursor[6]
        self.total = cursor[7]
    def __str__(self):
        string = 'code: '
        string = string + self.code +'\n'
        string = 'name: '
        string = string + self.name +'\n'
        string = 'increase: '
        string = string + self.increase +'\n'
        string = 'price: '
        string = string + self.price +'\n'
        string = 'pe: '
        string = string + self.pe +'\n'
        string = 'forcast: '
        string = string + self.forcast +'\n'
        string = 'pbv: '
        string = string + self.pbv +'\n'
        string = 'total: '
        string = string + self.total +'\n'
        return string
  