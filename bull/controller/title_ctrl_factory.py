#!/usr/bin/python  
# -*- coding: utf-8 -*-
from util.singleton import singleton
from dao.title_dao import TitleDao
from controller.title_ctrl import TitleCtrl

@singleton
class TitleCtrlFactory():
    def __init__(self,setting):
        self.setting = setting

    def create_title_ctrl(self,wrapper_id):
        setting = self.setting
        path = setting['title_path'][wrapper_id]
        
        dao = TitleDao(path)
        ctrl = TitleCtrl(dao)
        return ctrl