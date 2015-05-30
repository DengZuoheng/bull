#!/usr/bin/python  
# -*- coding: utf-8 -*-
from PyQt4 import QtGui
from PyQt4 import Qt  
from PyQt4 import QtCore  

class QHoverButton(QtGui.QWidget):
    def __init__(self,parent, image, image_active=None, width=24, height=24):
        super(QHoverButton, self).__init__(parent)
        self.image = image.scaled(width,height)
        self.image_active = image_active
        if(self.image_active==None):
            self.image_active = self.image
        else:
            self.image_active = image_active.scaled(width,height)
        self.__hover = False
        self.width = width
        self.height = height
        self.setMouseTracking(True)
        self.setMaximumSize(width,height)
        self.setMinimumSize(width,height)
        self.installEventFilter(self)
         
    def paintEvent(self,e):
        painter = QtGui.QPainter()
        painter.begin(self)
        self.__drawWidget(painter)
        painter.end()

    def __drawWidget(self,painter):
        if(self.__hover):
            painter.drawImage(
                QtCore.QPoint(0,0),self.image_active)
        else:
            painter.drawImage(
                QtCore.QPoint(0,0),self.image)

    def eventFilter(self, qobject, qevent):
        qtype = qevent.type()
        if qtype == QtCore.QEvent.Enter:
            self.__hover = True
            self.update()
        if qtype == QtCore.QEvent.Leave:
            self.__hover = False
            self.update()
        if qtype == QtCore.QEvent.MouseButtonPress:
            self.emit(QtCore.SIGNAL('clicked()'))
        
        return super(QHoverButton, self).eventFilter(qobject, qevent)
    
    def __in_btn_area(self,point):
        if 0 <= point.x() <= self.width and 0 <= point.y() <= self.height:
            return True
        return False

    def sizeHint( self ):
        return QtCore.QSize( self.width,self.height)