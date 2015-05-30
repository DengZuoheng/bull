#!/usr/bin/python  
# -*- coding: utf-8 -*-
import os
import sys
path = sys.path[0] 
parent_path = os.path.dirname(path) 
sys.path.insert(0,(parent_path))
from dao.title_dao import TitleDao

class ConditionWrapperCtrl():
    def __init__(self,view):
        self.view = view
        #id_map是指标简称和所分配的id的字典
        self.id_map = {}

    #将一个key和id加到id_map去
    def add2id_map(self,key,id):
        self.id_map[key]=id

    def get_title_list(self,setting):
        dao =  TitleDao(setting['title_base'])
        title_dict = setting['condition_wrapper_title_dict']
        raw_title = dao.load_title()
        title_list = []
        i = 0
        for key in title_dict :
            temp = '%s'%(raw_title[title_dict[key]])
            #title_list.append(raw_title[title_dict[key]])
            title_list.append(temp)
            self.add2id_map(key,i)
            i = i+1
        return title_list