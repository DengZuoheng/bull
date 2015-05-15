#!/usr/bin/python  
#-*-coding:utf-8-*-
import os
import sys
path = sys.path[0] 
parent_path = os.path.dirname(path) 
sys.path.insert(0,(parent_path))
from PyQt4 import QtGui
from dao.wencai_dao import WencaiDao
from controller.stock_ctrl import StockCtrl
from view.qresultdialog import QResultDialog

class ScreenerGroupCtrl():
    def __init__(self,view):
        self.view = view

    def get_data_list(self,setting):
        self.stock_ctrl = StockCtrl(WencaiDao(setting['db_path']))
        all_stock = self.stock_ctrl.all()
        title_dict = setting['condition_wrapper_title_dict']
        length = len(title_dict)
        ret = []
        for key in title_dict:
            ret.append({'data':[],'data_max':None,'data_min':None})
        for item in all_stock:
            i = 0
            for key in title_dict:           
                if item[key] is not None:
                    ret[i]['data'].append(item[key]) 
                    if ret[i]['data_max'] is None:
                        ret[i]['data_max'] = item[key]
                    elif ret[i]['data_max'] < item[key]:
                        ret[i]['data_max'] = item[key]
                    if ret[i]['data_min'] is None:
                        ret[i]['data_min'] = item[key]
                    elif ret[i]['data_min'] >item[key]:
                        ret[i]['data_min'] = item[key]
                i = i+1
        return ret

    def get_title_list(self,setting):
        return self.view.title_list

    def get_init_args(self,setting):
        args = [
            setting['screener_group_header'],
            self.get_title_list(setting),
            self.get_data_list(setting),
            setting['screener_group_title_text'],
            setting['screener_group_title_width'],
            setting['screener_save_text'],
            setting['screener_cancel_text'],
            setting['screener_submit_text'],
            QtGui.QImage(setting['range_slider_btn']),
            QtGui.QImage(setting['range_slider_btn_active']),
            QtGui.QImage(setting['screener_item_del_icon']),
            QtGui.QImage(setting['screener_item_del_icon_active']),
        ]
        return args

    def on_submit_event(self):
        id_map = self.view.condition_wrapper_ctrl.id_map
        condition_list = []
        for key in id_map:
            #2表示checked
            if self.view.condition_wrapper.get_nth_state(id_map[key]) == 2:
                ret = self.view.screener_group.get_nth_value(id_map[key])
                tu = (key,ret[0],ret[1])
                condition_list.append(tu)
        result = self.stock_ctrl.filter(condition_list)
        dlg_data = {
            'header':[u'股票代码',u'股票简称',u'涨跌幅',
            u'现价',u'市盈率',u'动态市盈率',u'市净率',u'总股本(亿)'],
            'data':result,
            'index_map':['ticker','title','change','price',
            'pe','peg','pbv','capital'],
            'row':len(result),#行
            'col':8,#列
            'color':{
                'near_selected_str':'#efefef',
                'normal_str':'#ffffff',
                'null_double':'#ffe5e5',
                'normal_double':'#f2e5ff',
                'near_selected_double':'#e2d5ef',
                'near_selected_null_double':'#efd5d5',
                'selected_double':'#a0cee4',
                'selected_str':'#a0cee4',
                'selected_null':'#a0cee4',
            }
        }
        dlg = QResultDialog(self.view,dlg_data)
        if dlg.exec_():
            print "dlg finish"
        print 'GGGGGGGGGGGGG'

    def on_cancel_event(self):
        self.view.condition_wrapper.reset()
        self.view.screener_group.reset()

    def on_save_event(self):
        print("save")