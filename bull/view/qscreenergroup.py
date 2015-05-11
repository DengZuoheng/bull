#!/usr/bin/python  
#-*-coding:utf-8-*-
import sys
from PyQt4 import QtGui
from PyQt4 import Qt  
from PyQt4 import QtCore  
from qscreeneritem import QScreenerItem

import pycurl
import StringIO
import urllib
import re
import json

class QScreenerGroup(QtGui.QFrame):
    def __init__(self,parent,title,title_list,data_list):
        super(QScreenerGroup,self).__init__(parent)
        self.title = title
        self.title_list = title_list
        self.data_list = data_list
        self.screener_list = []
        inner_frame = QtGui.QWidget()
        inner_layout = QtGui.QVBoxLayout(inner_frame)
        for i in range(len(title_list)):
            screener_item = QScreenerItem(self,
                self.title_list[i],
                self.data_list[i],
                i)
            inner_layout.addWidget(screener_item)

        scroll = QtGui.QScrollArea()
        scroll.setWidget(inner_frame)
        scroll.setWidgetResizable(True)
        scroll.setObjectName('ScreenerScroll')
        self.setStyleSheet("""
            QWidget#ScreenerScroll{
                border:none;
            }
            QScrollBar:horizontal {
                 border: 0px solid grey;
                 background: white;
                height:8px;
                margin: 0;
            }
            QScrollBar::handle:horizontal {
                background: grey;
                min-width: 10px;
            }
            QScrollBar::handle:horizontal:hover {
                background: #0066cc;
                min-width: 10px;
            }
            QScrollBar::add-line:horizontal {
                border: 2px solid grey;
                background: #32CC99;
                width: 20px;
                subcontrol-position: right;
                subcontrol-origin: margin;
            }

            QScrollBar::sub-line:horizontal {
                border: 2px solid grey;
                background: #32CC99;
                width: 20px;
                subcontrol-position: left;
                subcontrol-origin: margin;
            }

            QScrollBar:vertical{
                 border: 0px solid grey;
                 background: white;
                 width: 8px;
                 margin: 0;
             }
             
             QScrollBar::handle:vertical {
                 background: grey;
                 min-height: 20px;
             }
             QScrollBar::handle:vertical:hover {
                 background: #0066cc;
                 min-height: 20px;
             }
             QScrollBar::add-line:vertical {
                 border: 0px solid grey;
                 background: #32CC99;
                 height: 0;
                 subcontrol-position: bottom;
                 subcontrol-origin: margin;
             }

             QScrollBar::sub-line:vertical {
                 border: 0px solid grey;
                 background: #32CC99;
                 height: 0;
                 subcontrol-position: top;
                 subcontrol-origin: margin;
             }
             QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {
                 border: 0px solid grey;
                 width: 3px;
                 height: 0;
                 background: red;
             }

             QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
                 background: none;
             }
             .QPushButton{
                border-radius:2px;
                border:1px solid #006aca;
                background-color:#006aca;
                color:#fff;
                padding:6px 12px;
                margin-right:5px;
            }
            .QPushButton:hover{
                border-radius:2px;
                border:1px solid #0578eb;
                background-color:#0578eb;
                color:#fff;
                padding:6px 12px;
                margin-right:5px;
            }
            """)
        #scroll.setStyleSheet('border:none')
        layout = QtGui.QVBoxLayout()
        label = QtGui.QLabel(title)
        label.setStyleSheet('font-weight:bold;padding-left:5px;padding-bottom: 20px')
        layout.addWidget(label)
        hbox = QtGui.QHBoxLayout()
        label_name = QtGui.QLabel(u'条件')
        label_name.setStyleSheet('font-weight:bold;padding-left:5px;padding-left: 14px')
        label_name.setMinimumWidth(100)
        label_min = QtGui.QLabel(u'最小值')
        label_min.setStyleSheet('font-weight:bold;padding-left:5px;padding-left: 14px')
        label_min.setMinimumWidth(90)
        label_chart = QtGui.QLabel(u'条件范围/股票分布')
        label_chart.setStyleSheet('font-weight:bold;padding-left:5px;padding-left: 14px')
        label_chart.setMinimumWidth(50)
        label_chart.setAlignment(QtCore.Qt.AlignCenter)
        label_max = QtGui.QLabel(u'最大值')
        label_max.setStyleSheet('font-weight:bold;padding-left:5px;padding-left: 14px')
        label_max.setMinimumWidth(90)
        label_clode = QtGui.QLabel(u'删除')
        label_clode.setStyleSheet('font-weight:bold;padding-left:5px;padding-left: 14px')
        label_clode.setMinimumWidth(50)
        hbox.addWidget(label_name)
        hbox.addWidget(label_min)
        hbox.addWidget(label_chart)
        hbox.addWidget(label_max)
        hbox.addWidget(label_clode)
        layout.addLayout(hbox) 
        layout.addWidget(scroll)
        button_save = QtGui.QPushButton(u'收藏搜索条件')
        button_cancel = QtGui.QPushButton(u'重置')
        button_submit = QtGui.QPushButton(u'开始选股')
        button_layout= QtGui.QHBoxLayout()
        button_layout.addWidget(button_save)
        button_layout.addWidget(button_cancel)
        button_layout.addStretch()
        button_layout.addWidget(button_submit)
        layout.addLayout(button_layout)
        self.setLayout(layout)

class Example(QtGui.QWidget):
    def __init__(self):
        super(Example,self).__init__()
        self.initUI()

    def initUI(self):
        ret = [1,4,6,4,2,5,9,4,9]
        max_value = max(ret)
        min_value = min(ret)
        data = {
            'data':ret,
            'data_max':max_value,
            'data_min':min_value,
        }
        data_list = [{'data':ret,'data_max':max_value,'data_min':min_value}]*16
        title_list = [u'市盈率']*16
        self.wid = QScreenerGroup(self,u'筛选条件',title_list,data_list)
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
