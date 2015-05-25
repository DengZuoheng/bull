#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from PyQt4 import QtCore
from PyQt4 import QtGui
from qtabledataitem import QTableDataItem
from qhoverbutton import QHoverButton

class QResultDialog(QtGui.QDialog):
    def __init__(self,parent=None,data=None):
        super(QResultDialog,self).__init__(parent)
        self.data = data
        setting = self.data['setting']
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint |QtCore.Qt.Dialog)
        self.init_close_group() 
        self.init_label()
        if self.data['row'] == 0:
            self.init_no_result_warning()
        else:
            self.init_color()
            self.init_table()
            self.press_col = None
            self.press_row = None
            self.connect(self.table,
            QtCore.SIGNAL('cellPressed(int,int)'),
                self.on_cell_press)
        #hbox = QtGui.QHBoxLayout(self)
        #hbox.addWidget(self.table)
        self.setFixedWidth(setting['result_dialog_width'])
        self.setFixedHeight(setting['result_dialog_height'])

    def init_no_result_warning(self):
        text = self.data['setting']['no_result_warning_text']
        geometry = self.data['setting']['no_result_warning_geometry']
        self.no_result_label = QtGui.QLabel(text,self)
        self.no_result_label.setGeometry(*geometry)
        self.no_result_label.setAlignment(QtCore.Qt.AlignCenter)

    def init_label(self):
        total = self.data['row']
        setting = self.data['setting']
        self.label = QtGui.QLabel(setting['result_label']%total,self)
        self.label.setGeometry(*setting['result_label_geometry'])

    def init_close_group(self):
        setting = self.data['setting']
        close_btn_image = QtGui.QImage(setting['close_btn_image_path'])
        close_btn_image_active = QtGui.QImage(setting['close_btn_image_active_path'])
        self.close_btn = QHoverButton(self,close_btn_image,close_btn_image_active)
        self.close_btn.setGeometry(*setting['close_btn_geometry'])
        self.close_btn.setToolTip(setting['close_btn_tool_tip'])
        self.connect(self.close_btn,
                    QtCore.SIGNAL('clicked()'),
                    self.onCloseButtonClick)

    def init_color(self):
        self.color_map = {
            'near_selected_str':None,
            'normal_str':None,
            'null_double':None,
            'normal_double':None,
            'near_selected_double':None,
            'near_selected_null_double':None,
            'selected_double':None,
            'selected_str':None,
            'selected_null':None,
        }
        for key in self.color_map:
            self.color_map[key]=QtGui.QColor(self.data['color'][key])

    def init_table(self):
        data = self.data
        setting = self.data['setting']
        self.table = QtGui.QTableWidget(data['row'],data['col'],self)
        for n ,row in enumerate(data['data']):
            stock = data['data'][n]

            item_ticker = QTableDataItem('str',stock.ticker.decode('UTF-8'))
            self.table.setItem(n,0,item_ticker)
            self.reset_color(item_ticker)

            item_title = QTableDataItem('str',stock.title.decode('UTF-8'))
            self.table.setItem(n,1,item_title)
            self.reset_color(item_title)

            if stock.change is not None:
                item_change = QTableDataItem('double',str(stock.change))
            else:
                item_change = QTableDataItem('null','')
            item_change.setTextAlignment(
                QtCore.Qt.AlignRight|QtCore.Qt.AlignVCenter)

            self.table.setItem(n,2,item_change)
            self.reset_color(item_change)

            if stock.price is not None:
                item_price = QTableDataItem('double',str(stock.price))
            else:
                item_price = QTableDataItem('null','')
            item_price.setTextAlignment(
                QtCore.Qt.AlignRight|QtCore.Qt.AlignVCenter)

            self.table.setItem(n,3,item_price)
            self.reset_color(item_price)

            if stock.pe is not None:
                item_pe = QTableDataItem('double','%.04f'%stock.pe)
            else:
                item_pe  = QTableDataItem('null','')
            item_pe.setTextAlignment(
                QtCore.Qt.AlignRight|QtCore.Qt.AlignVCenter)

            self.table.setItem(n,4,item_pe)
            self.reset_color(item_pe)

            if stock.peg is not None:
                item_peg = QTableDataItem('double','%.04f'%stock.peg)
            else:
                item_peg = QTableDataItem('null','')
            item_peg.setTextAlignment(
                QtCore.Qt.AlignRight|QtCore.Qt.AlignVCenter)

            self.table.setItem(n,5,item_peg)
            self.reset_color(item_peg)

            if stock.pbv is not None:
                item_pbv = QTableDataItem('double','%.04f'%stock.pbv)
            else:
                item_pbv = QTableDataItem('null','')
            item_pbv.setTextAlignment(
                QtCore.Qt.AlignRight|QtCore.Qt.AlignVCenter)

            self.table.setItem(n,6,item_pbv)
            self.reset_color(item_pbv)

            if stock.capital is not None:
                temp = stock.capital
                if temp > 10000000:#大于千万
                    temp  = temp/100000000#除以亿
                item_capital = QTableDataItem('double','%.04f'%temp)
            item_capital.setTextAlignment(
                QtCore.Qt.AlignRight|QtCore.Qt.AlignVCenter)

            self.table.setItem(n,7,item_capital)
            self.reset_color(item_capital)

            self.table.setRowHeight(n,setting['result_table_row_height'])

        self.table.setHorizontalHeaderLabels(data['header'])
        self.table.verticalHeader().setVisible(False)
        self.table.setFocusPolicy(QtCore.Qt.NoFocus)
        #self.table.resizeColumnsToContents()
        self.table.setGeometry(*setting['result_table_geometry'])

    def on_cell_press(self,col,row):#行,列
        #还没被点击过
        if self.press_col is None and self.press_row is None:
            self.press_col = col
            self.press_row = row
            #将同一行设为指定颜色
            for i in range(self.data['col']):
                item = self.table.item(col,i)
                self.set_near_selected_color(item)
            #将同一列设为指定颜色
            for i in range(self.data['row']):
                item = self.table.item(i,row)
                self.set_near_selected_color(item)

        #点击了同一行,同一列
        elif self.press_col == col and self.press_row == row:
            pass
        #点击了同一行, 但不同一列
        elif self.press_col == col and self.press_row != row:
            for i in range(self.data['row']):
                #还原上一列的颜色设置
                item_old = self.table.item(i,self.press_row)
                self.reset_color(item_old)
                #设置这一列的颜色
                item_new = self.table.item(i,row)
                self.set_near_selected_color(item_new)  
            old_selected_item = self.table.item(self.press_col,self.press_row)
            self.set_near_selected_color(old_selected_item)
        #点击了同一列, 但是不同行
        elif self.press_col != col and self.press_row == row:
            for i in range(self.data['col']):
                #还原上一行的颜色设置
                item_old = self.table.item(self.press_col,i)
                self.reset_color(item_old)
                #设置这一行的颜色
                item_new  = self.table.item(col,i)
                self.set_near_selected_color(item_new) 
            old_selected_item = self.table.item(self.press_col,self.press_row)
            self.set_near_selected_color(old_selected_item)
        #行和列都不同了
        else:
            for i in range(self.data['row']):
                #还原上一列的颜色设置
                item_old = self.table.item(i,self.press_row)
                self.reset_color(item_old)          
            for i in range(self.data['col']):
                #还原上一行的颜色设置
                item_old = self.table.item(self.press_col,i)
                self.reset_color(item_old)             
            for i in range(self.data['row']):
                #设置这一列的颜色
                item_new = self.table.item(i,row)
                self.set_near_selected_color(item_new) 
            for i in range(self.data['col']):     
                #设置着一行的颜色
                item_new  = self.table.item(col,i)
                self.set_near_selected_color(item_new) 
        selected_item = self.table.item(col,row)
        self.set_selected_color(selected_item)
        self.press_col = col
        self.press_row = row

    def set_near_selected_color(self,item):
        if item.data_type() == 'str':
            item.setBackgroundColor(self.color_map['near_selected_str'])
        elif item.data_type() == 'null':
            item.setBackgroundColor(self.color_map['near_selected_null_double'])
        else:
            item.setBackgroundColor(self.color_map['near_selected_double'])

    def reset_color(self,item):
        if item.data_type() == 'str':
            item.setBackgroundColor(self.color_map['normal_str'])
        elif item.data_type() == 'null':
            item.setBackgroundColor(self.color_map['null_double'])
        else:
            item.setBackgroundColor(self.color_map['normal_double'])

    def set_selected_color(self,item):
        if item.data_type() == 'str':
            item.setBackgroundColor(self.color_map['selected_str'])
        elif item.data_type() == 'null':
            item.setBackgroundColor(self.color_map['selected_null'])
        else:
            item.setBackgroundColor(self.color_map['selected_double'])

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