#!/usr/bin/python  
# -*- coding: utf-8 -*-
from PyQt4 import QtGui
from PyQt4 import Qt  
from PyQt4 import QtCore
from util.singleton import singleton
from view.qcondition_wrapper import QConditionWrapper
from view.qfav_wrapper import QFavWrapper

@singleton
class WrapperFactory():
    def __init__(self,setting):
        self.setting = setting

    def create_wrapper(self,wrapper_id,main_window,dao=None):
        setting = self.setting
        if wrapper_id == 'wencai':#同花顺数据
            kwargs = {
                'wrapper_id': wrapper_id,
                'parent' : main_window,
                'title' : setting['wencai_condition_wrapper_header'],
                'title_list' : dao.get_indicator_title_list(),
                'id_list' : dao.get_indicator_id_list(),
            }
            condition_wrapper = QConditionWrapper(**kwargs)
            
        elif wrapper_id == 'xueqiu':#雪球数据
            kwargs = {
                'wrapper_id': wrapper_id,
                'parent': main_window,
                'title': setting['xueqiu_condition_wrapper_header'],
                'title_list':dao.get_indicator_title_list(),
                'id_list':dao.get_indicator_id_list(),
            }
            condition_wrapper = QConditionWrapper(**kwargs)
            
        elif wrapper_id == 'fav':#收藏
            kwargs = {
                'parent':main_window,
                'title':setting['fav_wrapper_header'],
                'fav_list':dao.fav_list,
                'setting':setting,
                'delete_btn_image':QtGui.QImage(setting['close_icon_path']),
            }
            condition_wrapper = QFavWrapper(**kwargs)

        condition_wrapper.setGeometry(*setting['condition_wrapper_geometry'])
        return condition_wrapper
