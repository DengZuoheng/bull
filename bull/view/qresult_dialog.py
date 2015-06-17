#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from PyQt4 import QtCore
from PyQt4 import QtGui
from qtable_data_item import QTableDataItem
from view.qbull_window import QBullWindow

class QResultDialog(QBullWindow):
    def __init__(self,parent=None,data=None):
        setting = data['setting']
        kwargs = {
            'parent':parent,
            'width':setting['result_dialog_width'],
            'height':setting['result_dialog_height'],
            'has_close':True,
            'has_mini':False,
            'setting':setting
        }
        super(QResultDialog,self).__init__(**kwargs)
        self.data = data
        self.setting = setting
        self.title_ctrl = data['title_ctrl']
        self.row = len(self.data['data'])
        self.col = len(self.title_ctrl.get_header_list())
        self.init_label()
        
        if self.row == 0:
            self.init_no_result_warning()
        else:
            self.init_color()
            self.init_table()
            self.press_col = None
            self.press_row = None
            self.connect(self.table,
            QtCore.SIGNAL('cellPressed(int,int)'),
                self.on_cell_press)

    def init_no_result_warning(self):
        text = self.data['setting']['no_result_warning_text']
        geometry = self.data['setting']['no_result_warning_geometry']
        self.no_result_label = QtGui.QLabel(text,self)
        self.no_result_label.setProperty('cls','big2')
        self.no_result_label.setGeometry(*geometry)
        self.no_result_label.setAlignment(QtCore.Qt.AlignCenter)

    def init_label(self):
        total = self.row
        source = self.data['source']
        setting = self.data['setting']
        self.label = QtGui.QLabel(setting['result_label']%(total,source),self)
        self.label.setGeometry(*setting['result_label_geometry'])

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
        header_title_list = self.title_ctrl.get_header_title_list()
        header_list = self.title_ctrl.get_header_list()
        header_prefix = self.title_ctrl.get_prefix()
        self.table = QtGui.QTableWidget(self.row,self.col,self)
        for n ,row in enumerate(data['data']):
            stock = data['data'][n]
            for m, raw_key in enumerate(header_list):
                #raw_key是这种:"wencai_pe", 所以要将"wencai_"替换掉
                key = raw_key.replace('%s_'%header_prefix,'')
                #让model自己判断type
                _type = stock.get_type_by_key(key)
                #如果_type是null的话, 就是空字符串了
                _str = ''
                raw_data = stock[key]
                if _type == 'double':
                    #如果是double, 只打印4位小数
                    if raw_data > 10000000:#大于千万
                        raw_data = raw_data/100000000#除以亿
                    _str = '%.4f'%raw_data
                elif _type == 'str':
                    _str = raw_data
                table_data_item = QTableDataItem(_type,_str)
                if _type == 'double':
                    #double型要右对齐
                    table_data_item.setTextAlignment(
                        QtCore.Qt.AlignRight|QtCore.Qt.AlignVCenter)
                self.table.setItem(n,m,table_data_item)
                self.reset_color(table_data_item)

            self.table.setRowHeight(n,setting['result_table_row_height'])

        self.table.setHorizontalHeaderLabels(header_title_list)
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
            for i in range(self.col):
                item = self.table.item(col,i)
                self.set_near_selected_color(item)
            #将同一列设为指定颜色
            for i in range(self.row):
                item = self.table.item(i,row)
                self.set_near_selected_color(item)

        #点击了同一行,同一列
        elif self.press_col == col and self.press_row == row:
            pass
        #点击了同一行, 但不同一列
        elif self.press_col == col and self.press_row != row:
            for i in range(self.row):
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
            for i in range(self.col):
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
            for i in range(self.row):
                #还原上一列的颜色设置
                item_old = self.table.item(i,self.press_row)
                self.reset_color(item_old)          
            for i in range(self.col):
                #还原上一行的颜色设置
                item_old = self.table.item(self.press_col,i)
                self.reset_color(item_old)             
            for i in range(self.row):
                #设置这一列的颜色
                item_new = self.table.item(i,row)
                self.set_near_selected_color(item_new) 
            for i in range(self.col):     
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
