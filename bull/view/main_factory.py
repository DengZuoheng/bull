#!/usr/bin/python  
# -*- coding: utf-8 -*-
from util.singleton import singleton
from view.wrapper_factory import WrapperFactory
from view.screener_factory import ScreenerFactory
from controller.main_ctrl import MainCtrl
from controller.index_list_ctrl import IndexListCtrl
from controller.fav_ctrl import FavCtrl
from controller.wrapper_ctrl import WrapperCtrl
from controller.stock_ctrl_factory import StockCtrlFactory
from controller.screener_ctrl import ScreenerCtrl
from dao.fav_dao import FavDao
   
@singleton
class MainFactory():
    def __init__(self, setting):
        self.setting = setting
        self.wrapper_factory = WrapperFactory(setting)
        self.screener_factory = ScreenerFactory(setting)

    def create_main_ctrl(self, main_window):
        main_ctrl = MainCtrl(main_window)
        return main_ctrl

    def create_index_list_ctrl(self, main_ctrl):
        index_list_ctrl = IndexListCtrl(main_ctrl, self.setting)
        return index_list_ctrl
    
    def create_wrapper_ctrl(self, wrapper_id, main_ctrl, setting):
        if wrapper_id == 'fav':
            dao = FavDao(setting['fav_path'])
            ctrl = FavCtrl(wrapper_id,main_ctrl, dao, setting)
            return ctrl
        else:
            ctrl = WrapperCtrl(wrapper_id, main_ctrl, setting)
            return ctrl

    def create_screener_ctrl(self, screener_id, main_ctrl, setting):
        setting = self.setting
        screener_ctrl = ScreenerCtrl(screener_id,main_ctrl,setting)
        return screener_ctrl

