#!/usr/bin/python  
#-*-coding:utf-8-*-
from dao.qss_dao import QSSDao
import setting 

class QSSCtrl():
    def __init__(self):
        self.dao = QSSDao(setting.QSS_PATH)

    def get_qss(self):
        return self.dao.load_qss()