#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Iwencai():
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
    def get_code(self):
        return self.code;
    def get_name(self):
        return self.name;
    def get_increase(self):
        return self.increase;
    def get_price(self):
        return self.price;
    def get_pe(self):
        return self.pe;
    def get_forcast(self):
        return self.forcast;
    def get_pbv(self):
        return self.pbv;
    def get_total(self):
        return self.total;
        
    def set_code(self,code):
        self.code = code;
    def set_name(self,name):
        self.name = name;
    def set_increase(self,increase):
        self.increase = increase;
    def set_price(self,price):
        self.price = price;
    def set_pe(self,pe):
        self.pe = pe;
    def set_forcast(self,forcast):
        self.forcast = forcast;
    def set_pbv(self,pbv):
        self.pbv = pbv;
    def set_total(self,total):
        self.total = total
     