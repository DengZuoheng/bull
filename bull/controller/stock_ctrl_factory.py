#!/usr/bin/python  
# -*- coding: utf-8 -*-
from dao.wencai_dao import WencaiDao
from dao.xueqiu_dao import XueqiuDao
from controller.stock_ctrl import StockCtrl
from model.wencai_stock import WencaiStock
from model.xueqiu_stock import XueqiuStock

class StockCtrlFactory():
    def __init__(self,setting):
        self.setting = setting

    def create_stock_ctrl(self,stock_type):
        setting = self.setting
        if stock_type == 'wencai':
            dao = WencaiDao(setting['db_path'],stock_type)
            ctrl = StockCtrl(setting,dao,WencaiStock,stock_type)
            return ctrl
        
        elif stock_type == 'xueqiu':
            dao = XueqiuDao(setting['db_path'],stock_type)
            ctrl = StockCtrl(setting,dao,XueqiuStock,stock_type)
            return ctrl
        