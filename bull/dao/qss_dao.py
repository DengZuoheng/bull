#!/usr/bin/python  
# -*- coding: utf-8 -*-
class QSSDao():
    def __init__(self,path="default.qss"):
        self.path = path

    def load_qss(self):
        f = open(self.path,'r')
        self.qss = f.read()
        f.close()
        return self.qss

    def store_qss(self,qss):
        f = open(self.path,'w')
        f.write(qss)
        f.close()