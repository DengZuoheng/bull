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

class ScreenerGroupCtrl():
    def __init__(self,view):
        self.view = view

    def get_data_list(self,setting):
        ctrl = StockCtrl(WencaiDao(setting['db_path']))
        all_stock = ctrl.all()
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