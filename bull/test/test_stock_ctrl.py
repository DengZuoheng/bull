#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
path = sys.path[0] 
parent_path = os.path.dirname(path) 
sys.path.insert(0,(parent_path))
import unittest
from controller.stock_ctrl import StockCtrl
from controller.setting_ctrl import SettingCtrl
from model.wencai_stock import WencaiStock
from model.xueqiu_stock import XueqiuStock

class stock_dao_mockup():
    def __init__(self):
        pass
    
    def filter(self,condition):
        result = []
        return result

    def update(self,result):
        pass

    def empty(self):
        return False

#即将废弃的
class Test_test_stock_ctrl(unittest.TestCase):
    def test_StockCtrl(self):
        setting_ctrl = SettingCtrl()
        setting = setting_ctrl.get_setting()
        stock_dao = stock_dao_mockup()
        stock_ctrl = StockCtrl(setting,stock_dao,WencaiStock,'weicai')
        stock_ctrl.all()
        stock_ctrl.filter([])
        #无参数的update会调用spider, 无网络环境下不应该测试
        #stock_ctrl.update()
        stock_ctrl.update_by_result([])

if __name__ == '__main__':
    unittest.main()
