#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from PyQt4 import QtCore
from PyQt4 import QtGui
from qbullmessagebox import QBullMessageBox
from qfocuslineedit import QFocusLineEdit

class QNewFavDlg(QBullMessageBox):
    def __init__(self, parent=None, data=None):
        super(QNewFavDlg,self).__init__(parent,data['title'],data['setting'])
        self.data = data
        self.setting = self.data['setting']
        self.initUI()

    def init_custom_group(self, layout):
        self.init_input_group()
        layout.addWidget(self.input_line_edit_label)
        layout.addWidget(self.input_line_edit)
        layout.addWidget(self.input_line_edit_warning)
        layout.addStretch()

    def init_input_group(self):
        label_text = self.setting['new_fav_input_label_text']
        self.input_line_edit_label = QtGui.QLabel(label_text, self)
        self.input_line_edit = QFocusLineEdit(self)
        self.input_line_edit.setFocus()
        self.input_line_edit_warning = QtGui.QLabel('',self)
        self.input_line_edit_warning.setProperty('cls','text_danger')
        self.connect(self.input_line_edit,
            QtCore.SIGNAL('focusIn()'),
            self.on_line_edit_focus_in)

    def on_cancel(self):
        self.value = None
        self.close()

    def on_submit(self):
        qstr = self.input_line_edit.text()
        if(len(qstr)==0):
            warning = self.setting['new_fav_no_input_warning']
            self.input_line_edit_warning.setText(u'warning')
        else:
            self.value = qstr
            self.close()

    def on_line_edit_focus_in(self):
        self.input_line_edit_warning.setText(u'')


