#!/usr/bin/python  
# -*- coding: utf-8 -*-
from dao.setting_dao import SettingDao
import setting 

class SettingCtrl():
    def __init__(self):
        self.dao = SettingDao(setting.SETTING_PATH)

    def get_setting(self):
        return self.dao.load_setting()