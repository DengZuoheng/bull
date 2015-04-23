#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
from abc import ABCMeta, abstractmethod
#path = os.getcwd()
path = sys.path[0] 
parent_path = os.path.dirname(path) 
sys.path.insert(0,(parent_path))

class Spider():
    def __init__(self):
        pass
        
    @abstractmethod
    def results(self):
        pass
       