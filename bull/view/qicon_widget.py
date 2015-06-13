#!/usr/bin/python  
# -*- coding: utf-8 -*-
from PyQt4 import QtGui
from PyQt4 import Qt  
from PyQt4 import QtCore 

class QIconWidget(QtGui.QFrame):
    def __init__(self,parent,text,icon,icon_size):
        super(QIconWidget,self).__init__(parent)
        self.text = text
        self.icon = icon
        self.icon_size = icon_size
        self.icon_screen = QtGui.QLabel(self)
        pixmap = QtGui.QPixmap(icon).scaled(icon_size[0],icon_size[1])
        self.icon_screen.setPixmap(pixmap)
        self.icon_screen.setFixedWidth(icon_size[0])
        self.icon_screen.setFixedHeight(icon_size[1])
        self.title = QtGui.QLabel(text,self)
        main_layout = QtGui.QHBoxLayout()
        main_layout.addWidget(self.icon_screen)
        main_layout.addWidget(self.title)
        self.setLayout(main_layout)