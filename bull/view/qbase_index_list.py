#!/usr/bin/python  
# -*- coding: utf-8 -*-
import sys
from PyQt4 import QtGui
from PyQt4 import Qt  
from PyQt4 import QtCore

class QBaseIndexList(QtGui.QFrame):
    def __init__(self,parent):
        super(QBaseIndexList, self).__init__(parent)