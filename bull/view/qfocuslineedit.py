#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from PyQt4 import QtCore
from PyQt4 import QtGui

class QFocusLineEdit(QtGui.QLineEdit):
    def __init__(self,parent=None):
        super(QFocusLineEdit,self).__init__(parent)

    def focusInEvent(self, event):
        self.emit(QtCore.SIGNAL('focusIn()'))

    def focusOutEvent(self,event):
        self.emit(QtCore.SIGNAL('focusOut()'))