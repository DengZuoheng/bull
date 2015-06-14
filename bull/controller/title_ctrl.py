#!/usr/bin/python  
# -*- coding: utf-8 -*-

class TitleCtrl():
    def __init__(self,title_dao):
        self.title_dao = title_dao
        self.title_struct = title_dao.load_title()

    #这个会获取所有title, 包括"股票简称"
    def get_title_list(self):
        ret = []
        for key in self.title_struct['title']:
            ret.append(self.title_struct['title'][key])
        return ret

    #获取用于筛选器的中文title
    def get_indicator_title_list(self):
        dic = self.get_indicator_dict()
        return dic.values()

    #获取结果表头的id
    def get_header_list(self):
        return self.title_struct['header']

    #获取结果表头的中文title
    def get_header_title_list(self):
        dic = self.title_struct['title']
        return [dic[item] for item in self.title_struct['header']]

    #这个会获取所有用于选择器的title的id, 不包括"股票简称"
    def get_indicator_id_list(self):
        dic = self.get_indicator_dict()
        return dic.keys()

    #这个会获取所有id
    def get_id_list(self):
        return self.title_struct['title'].keys()

    #这个获取所有title与id的字典, 包括"股票简称"
    def get_title_dict(self):
        return self.title_struct['title']

    #获取所有用于筛选器的id和title的字典
    def get_indicator_dict(self):
        ret = {}
        for key in self.title_struct['indicator']:
            ret[key] = self.title_struct['title'][key]
        return ret

    def get_prefix(self):
        return self.title_struct['prefix']