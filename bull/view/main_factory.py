#!/usr/bin/python  
# -*- coding: utf-8 -*-
from util.singleton import singleton
from view.wrapper_factory import WrapperFactory
from view.screener_factory import ScreenerFactory
from controller.main_ctrl import MainCtrl
from controller.index_list_ctrl import IndexListCtrl
from controller.fav_ctrl import FavCtrl
from controller.wrapper_ctrl import WrapperCtrl
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

    def create_index_list_ctrl(self, index_list, main_ctrl):
        index_list_ctrl = IndexListCtrl(main_ctrl, setting)
        return index_list_ctrl
    
    def create_wrapper_ctrl(self, wrapper_id, main_ctrl, setting):
        if wrapper.id == 'fav':
            dao = FavDao(setting['fav_path'])
            ctrl = FavCtrl(wrapper_id,main_ctrl, dao, setting)
            return ctrl
        else:
            ctrl = WrapperCtrl(wrapper_id, main_ctrl, setting)
            return ctrl

     def create_screener_ctrl(self, screener_id, main_ctrl, setting):
        setting = self.setting
        stock_ctrl_factory = StockCtrlFactory(self.setting)
        stock_ctrl = stock_ctrl_factory.create_stock_ctrl(screener_id)
        screener_ctrl = ScreenerCtrl(screener_id,main_ctrl,stock_ctrl)

