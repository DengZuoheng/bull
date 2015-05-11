#!/usr/bin/python  
#-*-coding:utf-8-*-
import sys
from PyQt4 import QtGui
from PyQt4 import Qt  
from PyQt4 import QtCore  
from qdistributionslider import QDistributionSlider
from qhoverbutton import QHoverButton

import pycurl
import StringIO
import urllib
import re
import json

class QScreenerItem(QtGui.QFrame):
    def __init__(self,parent,title,data,id):
        super(QScreenerItem,self).__init__(parent)
        self.title = title
        self.data = data
        self.id = id
        self.initUI()

    def initUI(self):
        #self.label2 = QtGui.QLabel('test',self)
        
        self.label = QtGui.QLabel(self.title,self)
        self.label.setMinimumWidth(100)
        self.distribution_slider = QDistributionSlider(self.data['data'],
            self.data['data_max'],
            self.data['data_min'])
        self.del_btn_img = QtGui.QImage('images/close_btn.png')
        self.del_btn_img_active = QtGui.QImage('images/close_btn.png')
        print(self.del_btn_img.width())
        self.delete_button = QHoverButton(self,
            self.del_btn_img,
            self.del_btn_img_active)
        self.layout = QtGui.QHBoxLayout(self)
        
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.distribution_slider)
        self.layout.addWidget(self.delete_button)

class example_spider():
    def __init__(self, base_url='http://www.iwencai.com/stockpick'):
        
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

    def result(self):
        buf1 = StringIO.StringIO()
        buf2 = StringIO.StringIO()
        c=pycurl.Curl()
        base_url = 'http://www.iwencai.com/stockpick'
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
        all_result = json.loads(response)
        data = all_result['list']

        #print all_result['list']
        return data

def example_result():

    sp = example_spider()
    ret = sp.result()
    l = []
    for item in ret:
        if item[3]=='--':
            continue
        l.append(float(item[3]))#现价
    return l

class Example(QtGui.QWidget):
    def __init__(self):
        super(Example,self).__init__()
        self.initUI()

    def initUI(self):
        ret = example_result()
        max_value = max(ret)
        min_value = min(ret)
        data = {
            'data':ret,
            'data_max':max_value,
            'data_min':min_value,
        }
        self.wid = QScreenerItem(self,u'测试',data,99)
        hbox = QtGui.QHBoxLayout()
        hbox.addWidget(self.wid)
        self.setLayout(hbox)
        self.setWindowTitle('QScreenerItem')
        self.setStyleSheet('background:#fff;')

def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    ex.show()
    app.exec_()

if __name__=='__main__':
    main()
