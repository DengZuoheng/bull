#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from PyQt4 import QtCore
from PyQt4 import QtGui
from qhoverbutton import QHoverButton

class QBullWindow(QtGui.QDialog):
    def __init__(self,parent,width,height,has_close=True,has_mini=False,setting={}):
        super(QBullWindow,self).__init__(parent)
        self.setting = setting
        self.width = width
        self.height = height
        self.has_close = has_close
        self.has_mini = has_mini
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint |QtCore.Qt.Dialog)
        self.init_close_group()
        self.setFixedWidth(self.width)
        self.setFixedHeight(self.height)

    def init_close_group(self):
        setting = self.setting
        if self.has_close:
            close_btn_image = QtGui.QImage(setting['close_btn_image_path'])
            close_btn_image_active = QtGui.QImage(setting['close_btn_image_active_path'])
            self.close_btn = QHoverButton(self,close_btn_image,close_btn_image_active)
            geo = [
                self.width-close_btn_image.width()-1,
                1,
                close_btn_image.width(),
                close_btn_image.height()
            ]
            self.close_btn.setGeometry(*geo)
            self.close_btn.setToolTip(setting['close_btn_tool_tip'])
            self.connect(self.close_btn,
                        QtCore.SIGNAL('clicked()'),
                        self.onCloseButtonClick)
        if self.has_mini:
            mini_btn_image = QtGui.QImage(setting['mini_btn_image_path'])
            mini_btn_image_active = QtGui.QImage(setting['mini_btn_image_active'])
            self.mini_btn = QHoverButton(self,mini_btn_image,mini_btn_image_active)
            if self.has_close:
                geo = [
                    self.width-mini_btn_image.width()-close_btn_image.width()-1,
                    1,
                    mini_btn_image.width(),
                    mini_btn_image.height()
                ]
            else:
                geo = [
                    self.width-mini_btn_image.width()-1,
                    1,
                    mini_btn_image.width(),
                    mini_btn_image.height()
                ]
            self.mini_btn.setGeometry(*geo)
            self.mini_btn.setToolTip(setting['mini_btn_tool_tip'])
            self.connect(self.mini_btn,
                         QtCore.SIGNAL('clicked()'),
                        self.onMinimizedButtonClick)  
        
    def onCloseButtonClick(self):
        self.close()
        
    def onMinimizedButtonClick(self):
        self.showMinimized()
         
    def mousePressEvent(self, event):
        try:
            if event.button() == QtCore.Qt.LeftButton:
                self.dragPosition = event.globalPos() - self.frameGeometry().topLeft()
                QtGui.QApplication.postEvent(self, QtCore.QEvent(174))
                event.accept()
        except:
            pass
     
    def mouseMoveEvent(self, event):
        if event.buttons() == QtCore.Qt.LeftButton:
            self.move(event.globalPos() - self.dragPosition)
            event.accept()