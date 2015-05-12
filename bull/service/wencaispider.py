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
from model.stock import Stock
from spider import Spider

class WencaiSpider(Spider):
    def __init__(self, 
                 base_url='http://www.iwencai.com/stockpick',
                 auto_perform = True):
        
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
        if auto_perform:
            self.perform()

    def perform(self):
        values = {
            'typed':'1',
            'preParams':'',
            'ts':'1',
            'f':'1',
            'qs':'1',
            'selfsectsn':'',
            'querytype':'',
            'searchfilter':'',
            'tid':'stockpick',
            'w':'pe',
        }
        
        #第一次请求获取含token的JSON
        url = self.base_url+'/search?%s'%(urllib.urlencode(values))
        self.curl.setopt(pycurl.URL, url)
        self.curl.setopt(pycurl.WRITEFUNCTION, self.buf_1.write)#设置回调
        self.curl.perform()
        
        res = re.findall(u'var allResult = (.*)?;',self.buf_1.getvalue())
        assert 1 == len(res)#应该只有一个符合结果
        token_obj = json.loads(res[0])
        
        #获取含token后请求一次拉取所有股票
        args = {
            'token': token_obj['token'],#token
            'p':1,#第几页
            'perpage':token_obj['total'],#每页多少股票
        }
        url = self.base_url+'/cache?%s'%(urllib.urlencode(args))
        self.curl.setopt(pycurl.URL, url)
        self.curl.setopt(pycurl.WRITEFUNCTION, self.buf_2.write)#设置回调
        self.curl.perform() 
        response = self.buf_2.getvalue()
        self.all_result = json.loads(response)

    def results(self):
        data = self.all_result['list']
        for item in data:
            arr = []
            item[0] = item[0].split('.')[0]
            arr.append(item[0])
            for id in range(1,8):
                if cmp('--',item[id]) == 0:
                    item[id] = None
                arr.append(item[id])
            self.save.append(Stock(*arr))
        return self.save
      
    def titles(self):
        return self.all_result['title']
      
    def detail(self,ticker):
        base_url = 'http://stockpage.10jqka.com.cn'
        url = base_url+'/spService/%s/Header/realHeader'%ticker
        detail_curl = pycurl.curl()
        curl.setopt(pycurl.CONNECTTIMEOUT,5)
        curl.setopt(pycurl.TIMEOUT,50)
        curl.setopt(pycurl.COOKIEFILE,'')
        curl.setopt(pycurl.FAILONERROR,True)
        curl.setopt(pycurl.URL,url)
        print url
            