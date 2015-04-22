#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
from abc import ABCMeta, abstractmethod
#path = os.getcwd()
path = sys.path[0] 
parent_path = os.path.dirname(path) 
sys.path.insert(0,(parent_path))
import pycurl
import StringIO
import urllib
import re
import json
from model.module import Module
class Spider():
    def __init__(self,base_url):
        self.base_url = base_url
        self.buf_1 = StringIO.StringIO()
        self.buf_2 = StringIO.StringIO()
        self.buf_3 = StringIO.StringIO()
        self.curl = pycurl.Curl()
        self.curl.setopt(pycurl.CONNECTTIMEOUT,5)
        self.curl.setopt(pycurl.TIMEOUT,50)
        self.curl.setopt(pycurl.COOKIEFILE,'')
        self.curl.setopt(pycurl.FAILONERROR,True)
        self.save = []
    @abstractmethod
    def spider(self):pass
       