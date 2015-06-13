#!/usr/bin/python  
# -*- coding: utf-8 -*-
"""
有change信号
有get_condition方法
"""
import sys
from PyQt4 import QtGui
from PyQt4 import Qt  
from PyQt4 import QtCore 

class QBaseWrapper(QtGui.QFrame):
    def __init__(self,parent):
        super(QBaseWrapper, self).__init__(parent)

    def get_condition(self):
        pass

    def set_condition(self):
        pass

    def should_connect_other(self):
        return False

    def connect_other_list(self):
        return []
        