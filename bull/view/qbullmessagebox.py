#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from PyQt4 import QtCore
from PyQt4 import QtGui
from view.qbullwindow import QBullWindow

class QBullMessageBox(QBullWindow):
    def __init__(self,parent=None,title='',setting={}):
        kwargs = {
            'parent':parent,
            'width':setting['bull_msg_box_width'],
            'height':setting['bull_msg_box_height'],
            'has_close':True,
            'has_mini':False,
            'setting':setting,
        }
        super(QBullMessageBox,self).__init__(**kwargs)
        self.title_text = title
        self.setting = setting
        self.value = False

    def initUI(self):
        self.init_title()
        self.init_button_group()
        hbox = QtGui.QHBoxLayout()
        hbox.addStretch()
        hbox.addWidget(self.submit_button)
        hbox.addWidget(self.cancel_button)
        vbox = QtGui.QVBoxLayout()
        self.layout_group_widget = QtGui.QWidget(self)
        self.init_custom_group(vbox)
        vbox.addLayout(hbox)
        self.layout_group_widget.setLayout(vbox)
        geo = self.setting['bull_msg_box_geometry']
        self.layout_group_widget.setGeometry(*geo)

    def init_custom_group(self,layout):
        pass

    def init_button_group(self):
        submit_btn_text = self.setting['bull_msg_box_submit_text']
        self.submit_button = QtGui.QPushButton(submit_btn_text,self)
        cancel_btn_text = self.setting['bull_msg_box_cancel_text']
        self.cancel_button = QtGui.QPushButton(cancel_btn_text,self)
        self.cancel_button.setProperty('cls','default')
        self.connect(self.submit_button,
            QtCore.SIGNAL('clicked()'),
            self.on_submit)

        self.connect(self.cancel_button,
            QtCore.SIGNAL('clicked()'),
            self.on_cancel)

    def init_title(self):
        self.title_label = QtGui.QLabel(self.title_text,self)
        geo = self.setting['warning_msg_box_title_geometry']
        self.title_label.setGeometry(*geo)
        self.title_label.setProperty('cls','dlg_title')

    def on_cancel(self):
        self.value = False
        self.close()

    def on_submit(self):
        self.value = True
        self.close()

    def get_value(self):
        return self.value

