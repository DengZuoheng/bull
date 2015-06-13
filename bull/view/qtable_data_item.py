#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from PyQt4 import QtCore
from PyQt4 import QtGui

class QTableDataItem(QtGui.QTableWidgetItem):
    def __init__(self,data_type,text):
        super(QTableDataItem,self).__init__(text)
        self.__data_type = data_type

    def data_type(self):
        return self.__data_type