#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from PyQt4 import QtCore
from PyQt4 import QtGui
from qtabledataitem import QTableDataItem
from qhoverbutton import QHoverButton

class QWarningMessageBox(QtGui.QDialog):
    def __init__(self, parent=None, data=None):
        super(QWarningMessageBox,self).__init__(parent)
        self.data = data
        self.setting = self.data['setting']
        self.title_text = self.setting['warning_msgbox_title']
        self.warning_text = data['warning_text']
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint |QtCore.Qt.Dialog)
        self.init_close_group() 
        self.init_title()
        self.init_warning_pic()
        self.init_warning_text()
        self.init_confirm_button_group()#一个按钮应该就可以了
        #TODO:关闭的快捷键
        self.setFixedWidth(self.setting['warning_msg_box_width'])
        self.setFixedHeight(self.setting['warning_msg_box_height'])

    def init_warning_pic(self):
        setting = self.setting
        self.warning_pic_screen = QtGui.QLabel(self)
        pixmap = QtGui.QPixmap(setting['warning_img_path'])
        pixmap = pixmap.scaled(*setting['warning_msg_icon_scaled'])
        self.warning_pic_screen.setPixmap(pixmap)
        self.warning_pic_screen.setGeometry(*setting['warning_msg_icon_geometry'])

    def init_warning_text(self):
        setting = self.setting
        self.warning_text_label = QtGui.QLabel(self.warning_text,self)
        self.warning_text_label.setWordWrap(True)
        self.warning_text_label.setGeometry(*setting['warning_msg_text_geometry'])

    def init_confirm_button_group(self):
        setting = self.setting
        text = setting['warning_msg_confirm_btn_label']
        self.button_ok = QtGui.QPushButton(text,self)
        geo = setting['warning_msg_confirm_btn_geometry']
        self.button_ok.setGeometry(*geo)
        self.connect(self.button_ok,
            QtCore.SIGNAL('clicked()'),
            self.close)

    def init_title(self):
        self.title_label = QtGui.QLabel(self.title_text,self)
        geo = self.setting['warning_msg_box_title_geometry']
        self.title_label.setGeometry(*geo)
        self.title_label.setProperty('cls','title')

    def init_close_group(self):
        setting = self.data['setting']
        close_btn_image = QtGui.QImage(setting['close_btn_image_path'])
        close_btn_image_active = QtGui.QImage(setting['close_btn_image_active_path'])
        self.close_btn = QHoverButton(self,close_btn_image,close_btn_image_active)
        geo = setting['warning_msg_close_btn_geometry']
        self.close_btn.setGeometry(*geo)
        self.close_btn.setToolTip(setting['close_btn_tool_tip'])
        self.connect(self.close_btn,
                    QtCore.SIGNAL('clicked()'),
                    self.onCloseButtonClick)

    def onCloseButtonClick(self):
        self.close()
        
    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.dragPosition = event.globalPos() - self.frameGeometry().topLeft()
            QtGui.QApplication.postEvent(self, QtCore.QEvent(174))
            event.accept()
 
    def mouseMoveEvent(self, event):
        if event.buttons() == QtCore.Qt.LeftButton:
            self.move(event.globalPos() - self.dragPosition)
            event.accept()