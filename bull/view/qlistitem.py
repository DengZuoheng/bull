#!/usr/bin/python  
# -*- coding: utf-8 -*-
from PyQt4 import QtGui
from PyQt4 import Qt  
from PyQt4 import QtCore  

class QListItem(QtGui.QFrame):
    def __init__(self,parent,title,image,id):
        super(QListItem,self).__init__(parent)
        self.title = title
        self.image = image
        self.id = id #when it was click , return an id
        #init ui
        title_label = QtGui.QLabel(title)
        icon_label = QtGui.QLabel()     
        icon_label.setPixmap(image)
        hbox = QtGui.QHBoxLayout()
        hbox.addWidget(icon_label)
        hbox.addWidget(title_label)
        self.setLayout(hbox)
    
    def mousePressEvent(self,QMouseEvent):
        self.emit(QtCore.SIGNAL('clicked(int)'),self.id)
        return super(QListItem,self).mousePressEvent(QMouseEvent)

    def enterEvent(self,QEvent):
        self.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        return super(QListItem, self).enterEvent(QEvent)

    def leaveEvent(self,QEvent):
        self.unsetCursor()
        return super(QListItem, self).leaveEvent(QEvent)

