#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from PyQt4 import QtCore
from PyQt4 import QtGui
from qbullmessagebox import QBullMessageBox

class QConfirmMessageBox(QBullMessageBox):
    def __init__(self,parent=None,data=None):
        super(QConfirmMessageBox,self).__init__(parent,data['title_text'],data['setting'])
        self.data = data
        self.setting = self.data['setting']
        self.main_confirm_text = data['main_confirm_text']
        self.confirm_tips = data['confirm_tips']
        self.confirm = False
        self.initUI()

    def init_custom_group(self, layout):
        self.init_context_group()
        layout.addWidget(self.main_confirm_label)
        layout.addWidget(self.confirm_tips)
        layout.addStretch()

    def init_context_group(self):
        self.main_confirm_label = QtGui.QLabel(self.main_confirm_text)
        self.main_confirm_label.setAlignment(QtCore.Qt.AlignHCenter)
        self.main_confirm_label.setProperty('cls','main_confirm_label')
        self.confirm_tips = QtGui.QLabel(self.confirm_tips)
        self.confirm_tips.setAlignment(QtCore.Qt.AlignHCenter)
        self.confirm_tips.setProperty('cls','confirm_tips')

    def get_confirm(self):
        return self.get_value()

    