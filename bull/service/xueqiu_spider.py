#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
path = sys.path[0] 
parent_path = os.path.dirname(path) 
sys.path.insert(0,(parent_path))

import pycurl
import StringIO
import urllib
import re
import json
from spider import Spider

class XueqiuSpider(Spider):
    def __init__(self, 
                 prepare_url='http://xueqiu.com/hq/screener',
                 base_url='http://xueqiu.com/stock/screener',
                 auto_perform = True):
        self.prepare_url = prepare_url;
        self.base_url = base_url
        self.buf_1 = StringIO.StringIO()
        self.buf_2 = StringIO.StringIO()
        self.curl = pycurl.Curl()
        self.curl.setopt(pycurl.USERAGENT, "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322)")
        self.curl.setopt(pycurl.CONNECTTIMEOUT,5)
        self.curl.setopt(pycurl.TIMEOUT,50)
        self.curl.setopt(pycurl.COOKIEFILE,'')
        self.curl.setopt(pycurl.FAILONERROR,True)
        self.save = []
        self.ctrl = None
        if auto_perform:
            self.perform()

    def set_call_back(self,ctrl):
        self.ctrl = ctrl

    def call_back(self):
        if self.ctrl != None:
            self.ctrl.call_back()

    def perform(self):
      
        values = {
            'category':'SH',
            'orderby':'symbol',
            'order':'desc',
        }
        
        #第一次请求获取含token的JSON
        url = self.prepare_url
        self.curl.setopt(pycurl.URL, url)
        self.curl.perform()
        
        self.call_back()
        
        #获取含token后请求一次拉取所有股票
        args = {
            'size':'1'
        }
        args.update(values)
        url = self.base_url+'/screen.json?%s'%(urllib.urlencode(args))
        self.curl.setopt(pycurl.URL, url)
        self.curl.setopt(pycurl.WRITEFUNCTION, self.buf_1.write)#设置回调
        self.curl.perform() 
        self.call_back()
        
        response = self.buf_1.getvalue()
        self.all_result = json.loads(response)
        args['size'] = self.all_result['count']
        
        url = self.base_url+'/screen.json?%s'%(urllib.urlencode(args))
        self.curl.setopt(pycurl.URL, url)
        self.curl.setopt(pycurl.WRITEFUNCTION, self.buf_2.write)#设置回调
        self.curl.perform() 
        self.call_back()
        
        response = self.buf_2.getvalue()
        self.all_result = json.loads(response)
        self.call_back()

    def results(self):
        data = self.all_result['list']#雪球的是list
        print data
        for item in data:
            arr = []
            item[0] = item[0].split('.')[0]
            arr.append(item[0])
            for id in range(1,8):
                if cmp('--',item[id]) == 0:
                    item[id] = None
                arr.append(item[id])
        return self.save
      
  
            