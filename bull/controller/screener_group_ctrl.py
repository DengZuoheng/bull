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
from view.qresult_dialog import QResultDialog
from view.qnew_fav_dlg import QNewFavDlg

class ScreenerGroupCtrl(QtCore.QObject):
    def __init__(self,screener_ctrl_list,main_ctrl):
        self.screener_ctrl_list = screener_ctrl_list
        self.main_ctrl = main_ctrl
        self.screener_id = screener_ctrl_list[0].screener_id

    def get_condition(self):
        return self.get_screener_by_id(self.screener_id).get_condition()

    def set_condition(self,condition):
        screener = self.get_screener_by_id(self.screener_id)
        screener.set_condition(condition)

    def start(self):
        for item in self.screener_ctrl_list:
            if item.screener_id == self.screener_id:
                item.set_screener_visible(True)
            else:
                item.set_screener_visible(False)

    def set_screener_id(self,new_id):
        if new_id == None:
            return 
        self.screener_id = new_id
        self.start()

    def get_screener_by_id(self,screener_id):
        for item in self.screener_ctrl_list:
            if item.screener_id == self.screener_id:
                return item

   