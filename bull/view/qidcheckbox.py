#!/usr/bin/python  
# -*- coding: utf-8 -*-
import sys
from PyQt4 import QtGui
from PyQt4 import Qt  
from PyQt4 import QtCore 

class QIDCheckBox(QtGui.QCheckBox):
    def __init__(self,text,parent,id):
        super(QIDCheckBox,self).__init__(text,parent)
        self.id = id
        self.connect(self,
                     QtCore.SIGNAL('stateChanged(int)'),
                     self.onStateChanged)

    def onStateChanged(self,state):
        self.emit(QtCore.SIGNAL('changed(int,int)'),state,self.id)

