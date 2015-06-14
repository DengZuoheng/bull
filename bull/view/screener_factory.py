#!/usr/bin/python  
# -*- coding: utf-8 -*-
import sys
from PyQt4 import QtGui
from PyQt4 import Qt  
from PyQt4 import QtCore
from view.qindex_list import QIndexList
from view.qscreener import QScreener
from util.singleton import singleton

@singleton
class ScreenerFactory():
    def __init__(self,setting):
        self.setting = setting

    def create_screener(self, main_window, screener_id, stock_ctrl, title_ctrl):
        setting = self.setting
        base_kwargs = {
            'parent':main_window,
            'header':setting['screener_group_header'][screener_id],
            'screener_id':screener_id,
            'title_list':title_ctrl.get_indicator_title_list(),
            'data_list':stock_ctrl.get_data_list(title_ctrl),
            'id_list':title_ctrl.get_indicator_id_list(),
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
        screener = QScreener(**base_kwargs)
        screener.setGeometry(*setting['screener_group_geometry'])
        return screener
        

