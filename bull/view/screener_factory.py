#!/usr/bin/python  
# -*- coding: utf-8 -*-
import sys
from PyQt4 import QtGui
from PyQt4 import Qt  
from PyQt4 import QtCore
from view.qindex_list import QIndexList
from util.singleton import singleton

@singleton
class ScreenerFactory():
    def __init__(self,setting):
        self.setting = setting

    def create_screener(self, main_window, screener_id, stock_ctrl, title_ctrl):
        setting = self.setting
        base_kwargs = {
            'header':setting['%s_screener_group_header'%screener_id],
            'screener_id':screener_id,
            'title_list':self.get_title_list(title_ctrl),
            'data_list':self.get_data_list(title_ctrl, stock_ctrl),
            'id_list':self.get_id_list(title_ctrl),
            'label_text_list':setting['screener_group_title_text'],
            'label_width_list':setting['screener_group_title_width'],
            'save_btn_alt':setting['screener_save_text'],
            'cancel_btn_alt':setting['screener_cancel_text'],
            'submit_btn_alt':setting['screener_submit_text'],
            'range_btn_img':QtGui.QImage(setting['range_slider_btn']),
            'range_btn_img_active':QtGui.QImage(setting['range_slider_btn_active']),
            'screener_item_del_icon':QtGui.QImage(setting['screener_item_del_icon']),
            'screener_item_del_icon_active':QtGui.QImage(setting['screener_item_del_icon_active']),
            'no_select_warning_main':setting['no_select_warning_main'],
            'no_select_warning_tip':setting['no_select_warning_tip'],
        }
        screener = QScrennerGroup(**base_kwargs)
        screener.setGeometry(*setting['screener_group_geometry'])
        return screener

    def get_title_list(self,title_ctrl):
        return title_ctrl.get_title_list()

    def get_id_list(self,title_ctrl):
        return title_ctrl.get_id_list()

    def get_data_list(self,title_ctrl, stock_ctrl):
        all_stock = stock_ctrl.all()
        title_dict = title_ctrl.get_title_dict()
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

