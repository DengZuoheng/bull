#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from PyQt4 import QtCore
from PyQt4 import QtGui
from qtabledataitem import QTableDataItem

class QResultDialog(QtGui.QDialog):
    def __init__(self,parent=None,data=None):
        super(QResultDialog,self).__init__(parent)
        self.data = data
        self.init_color()
        self.init_table()
        hbox = QtGui.QHBoxLayout(self)
        hbox.addWidget(self.table)
        self.setFixedWidth(871)
        self.setFixedHeight(490)
        
        self.press_col = None
        self.press_row = None
        self.connect(self.table,
            QtCore.SIGNAL('cellPressed(int,int)'),
            self.on_cell_press)

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
        self.table = QtGui.QTableWidget(data['row'],data['col'])
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
            item_change.setTextAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignVCenter)
            self.table.setItem(n,2,item_change)
            self.reset_color(item_change)

            if stock.price is not None:
                item_price = QTableDataItem('double',str(stock.price))
            else:
                item_price = QTableDataItem('null','')
            item_price.setTextAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignVCenter)
            self.table.setItem(n,3,item_price)
            self.reset_color(item_price)

            if stock.pe is not None:
                item_pe = QTableDataItem('double','%.04f'%stock.pe)
            else:
                item_pe  = QTableDataItem('null','')
            item_pe.setTextAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignVCenter)
            self.table.setItem(n,4,item_pe)
            self.reset_color(item_pe)

            if stock.peg is not None:
                item_peg = QTableDataItem('double','%.04f'%stock.peg)
            else:
                item_peg = QTableDataItem('null','')
            item_peg.setTextAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignVCenter)
            self.table.setItem(n,5,item_peg)
            self.reset_color(item_peg)

            if stock.pbv is not None:
                item_pbv = QTableDataItem('double','%.04f'%stock.pbv)
            else:
                item_pbv = QTableDataItem('null','')
            item_pbv.setTextAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignVCenter)
            self.table.setItem(n,6,item_pbv)
            self.reset_color(item_pbv)

            if stock.capital is not None:
                temp = stock.capital
                if temp > 10000000:#大于千万
                    temp  = temp/100000000#除以亿
                item_capital = QTableDataItem('double','%.04f'%temp)
            item_capital.setTextAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignVCenter)
            self.table.setItem(n,7,item_capital)
            self.reset_color(item_capital)

            self.table.setRowHeight(n,20)

        self.table.setHorizontalHeaderLabels(data['header'])
        self.table.verticalHeader().setVisible(False)
        self.table.setFocusPolicy(QtCore.Qt.NoFocus)
            

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
        print col,row

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