#!/usr/bin/python  
# -*- coding: utf-8 -*-
import os
import sys
path = sys.path[0] 
parent_path = os.path.dirname(path) 
sys.path.insert(0,(parent_path))
from PyQt4 import QtGui
from dao.wencai_dao import WencaiDao
from controller.stock_ctrl import StockCtrl
from view.qresultdialog import QResultDialog
from view.qnewfavdlg import QNewFavDlg

class ScreenerGroupCtrl():
    def __init__(self,view,setting=None):
        if setting == None:
            self.setting = view.setting
        else:
            self.setting = setting
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
            setting['no_select_warning_main'],
            setting['no_select-warning_tip'],
        ]
        return args

    def get_condition_list(self):
        id_map = self.view.condition_wrapper_ctrl.id_map
        condition_list = []
        for key in id_map:
            #2表示checked
            if self.view.condition_wrapper.get_nth_state(id_map[key]) == 2:
                ret = self.view.screener_group.get_nth_value(id_map[key])
                tu = (key,ret[0],ret[1])
                condition_list.append(tu)
        return condition_list

    def on_submit_event(self):
        id_map = self.view.condition_wrapper_ctrl.id_map
        condition_list = self.get_condition_list()
        result = self.stock_ctrl.filter(condition_list)
        dlg_data = {
            'header':self.setting['result_header'],
            'data':result,
            'index_map':self.setting['result_index_map'],
            'row':len(result),#行
            'col':len(self.setting['result_header']),#列
            'color':self.setting['result_color'],
            'setting':self.setting,
        }
        dlg = QResultDialog(self.view,dlg_data)
        dlg.exec_()

    def on_cancel_event(self):
        self.view.condition_wrapper.reset()
        self.view.screener_group.reset()

    def on_save_event(self):
        dlg_data = {
            'title':self.setting['new_fav_dlg_title'],
            'setting':self.setting,
        }
        dlg = QNewFavDlg(self.view,dlg_data)
        dlg.exec_()
        value = dlg.get_value()
        if value != None and value != False:
            condition_list = self.get_condition_list()
            fav_ctrl = self.view.fav_ctrl
            fav_ctrl.new_fav(value,condition_list)

    def update_data(self):
        data_list = self.get_data_list(self.setting)
        self.view.screener_group.update_data_list(data_list)