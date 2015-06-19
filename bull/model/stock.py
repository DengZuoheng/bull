#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
from abc import ABCMeta, abstractmethod
#path = os.getcwd()
path = sys.path[0] 
parent_path = os.path.dirname(path) 
sys.path.insert(0,(parent_path))

class Stock(object):
    def __init__(self):
        super(Stock,self).__init__()

    @abstractmethod
    def get_type_by_key(self,key):
        pass

    def __getitem__(self,key):
        return self.__dict__[key]