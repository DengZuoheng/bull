#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

class FavDao():
    def __init__(self,path = 'fav.json'):
        self.path = path

    def load_fav(self):
        f = open(self.path,'r')
        json_str = f.read()
        self.fav = json.loads(json_str)
        for i in range(len(self.fav)):
            for j in range(len(self.fav[i]['condition'])):
                #将列表转换为tuple, 以便传递给stock_dao
                self.fav[i]['condition'][j] = tuple(self.fav[i]['condition'][j])
        f.close()
        return self.fav

    def store_fav(self,fav):
        f = open(self.path,'w')
        f.write(json.dumps(fav))
        f.close()
        
