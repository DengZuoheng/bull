#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from PyQt4 import QtCore,QtGui
from qrangeslider import QRangeSlider

import pycurl
import StringIO
import urllib
import re
import json

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

class QDistributionSlider(QtGui.QWidget):
    def __init__(self,
            data,
            data_max,
            data_min,
            range_slider_width = 160,
            line_edit_width = 80,
            width = 335,
            height = 30,
            lvalue = 0.0,
            rvalue = 1.0):
        super(QDistributionSlider,self).__init__()
        self.width = width
        self.height = height
        self.lvalue = lvalue
        self.rvalue = rvalue
        self.data = data
        self.data_max = data_max
        self.data_min = data_min
        self.range_slider_width = range_slider_width
        self.line_edit_width = line_edit_width
        self.__initUI()

    def __uniformization(self):
        dis = [0]*self.range_slider_width
        e = float((self.data_max - self.data_min))/self.range_slider_width
        for i in self.data:
            idx = int(i/e) -2
            dis[idx-1] = dis[idx-1]+1
        max_value = max(dis)
        for i in range(len(dis)):
            dis[i] = float(dis[i]/max_value)
        return dis

    def __initUI(self):
        self.setMinimumSize(self.width,self.height)
        dis = self.__uniformization()
        self.range_slider = QRangeSlider(
            width=self.range_slider_width,
            height=self.height,
            distribution = dis,
            lvalue = self.lvalue,
            rvalue = self.rvalue,
            lbtn_image=QtGui.QImage('c:/Projects/bull/bull/images/drag_btn.png'),
            lbtn_image_active=QtGui.QImage('c:/Projects/bull/bull/images/drag_btn_active.png'))
        
        self.left_edit = QtGui.QLineEdit(self)
        self.left_edit.setFixedWidth(self.line_edit_width)
        self.left_edit.setFixedHeight(self.height)
        self.left_edit.setAlignment(QtCore.Qt.AlignCenter)
        
        self.right_edit = QtGui.QLineEdit(self)
        self.right_edit.setFixedWidth(self.line_edit_width)
        self.right_edit.setFixedHeight(self.height)
        self.right_edit.setAlignment(QtCore.Qt.AlignCenter)

        regexp = QtCore.QRegExp('^[0-9]*\.[0-9]*$')
        validator = QtGui.QRegExpValidator(regexp)
        self.left_edit.setValidator(validator)
        self.right_edit.setValidator(validator)

        self.left_edit.setText('%f'%(self.lvalue*self.data_max))
        self.right_edit.setText('%f'%(self.rvalue*self.data_max))

        hbox = QtGui.QHBoxLayout()
        hbox.setContentsMargins(0, 0, 0, 0)
        hbox.addWidget(self.left_edit)
        hbox.addWidget(self.range_slider)
        hbox.addWidget(self.right_edit)
        self.setLayout(hbox)
        self.connect(self.range_slider,
            QtCore.SIGNAL('focusIn(QFocusEvent)'),
            self.range_slider_focused)
        self.connect(self.range_slider, 
            QtCore.SIGNAL('valueChanged(float,float)'),
            self.changeRange)
        self.connect(self.left_edit,
            QtCore.SIGNAL('textEdited(const QString&)'),
            self.left_edit_press)
        self.connect(self.right_edit,
            QtCore.SIGNAL('textEdited(const QString&)'),
            self.right_edit_press)

    def left_edit_press(self, qstr):
        if(qstr==''):
            self.lvalue = 0
        else:
            self.lvalue = float(qstr)
        if(self.lvalue>self.rvalue):
            if(self.lvalue>=1):
                self.lvalue = 1
            self.rvalue = self.lvalue
        self.range_slider.setValue(self.lvalue,self.rvalue)

    def right_edit_press(self, qstr):
        if(qstr==''):
            self.rvalue = 0
        else:
            self.rvalue = float(qstr)
        if(self.rvalue<self.lvalue):
            if(self.rvalue<=0):
                self.rvalue = 0
            self.lvalue = self.rvalue
        self.range_slider.setValue(self.lvalue,self.rvalue)

    def range_slider_focused(self):
        self.left_edit.clearFocus()
        self.right_edit.clearFocus()

    def changeRange(self,lvalue,rvalue):
        self.lvalue = lvalue
        self.rvalue = rvalue
        self.left_edit.setText('%f'%(lvalue*self.data_max))
        self.right_edit.setText('%f'%(rvalue*self.data_max))


class Example(QtGui.QWidget):
    def __init__(self):
        super(Example,self).__init__()
        self.initUI()

    def initUI(self):
        ret = example_result()
        max_value = max(ret)
        min_value = min(ret)
        self.wid = QDistributionSlider(ret,max_value,min_value)
        hbox = QtGui.QHBoxLayout()
        hbox.addWidget(self.wid)
        self.setLayout(hbox)
        self.setGeometry(300, 300, 200, 40)
        self.setWindowTitle('QDistributionSlider')

def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    ex.show()
    app.exec_()

if __name__=='__main__':
    main()




