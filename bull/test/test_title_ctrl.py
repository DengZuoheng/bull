#!/usr/bin/env python
# -*- coding: utf-8 -*-
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
path = sys.path[0]
parent_path = os.path.dirname(path)
sys.path.insert(0,(parent_path))
import unittest
from dao.title_dao import TitleDao
from controller.title_ctrl import TitleCtrl

class Test_test_title_ctrl(unittest.TestCase):
    def test_TitleCtrl(self):
        dao = TitleDao('wencai_title.json')
        ctrl = TitleCtrl(dao)
        title_list = ctrl.get_title_list()
        if not isinstance(title_list,list):
            raise Exception('title_list is not a list')
        for item in title_list:
            if not isinstance(item,unicode):
                raise Exception('title_list item is not a str')
        indicator_title_list = ctrl.get_indicator_title_list()
        if not isinstance(indicator_title_list,list):
            raise Exception('indicator_title_list is not a list')
        for item in indicator_title_list:
            if not isinstance(item,unicode):
                raise Exception('indicator_title_list item is not a str')
        header_list = ctrl.get_header_list()
        if not isinstance(header_list,list):
            raise Exception('header_list is not a list')
        for item in header_list:
            if not isinstance(item,unicode):
                raise Exception('header_list item is not a str')
        header_title_list = ctrl.get_header_title_list()
        if not isinstance(header_title_list,list):
            raise Exception('header_title_list is not a list')
        for item in header_title_list:
            if not isinstance(item,unicode):
                raise Exception('header_title_list item is not a str')
        indicator_id_list = ctrl.get_indicator_id_list()
        if not isinstance(indicator_id_list,list):
            raise Exception('indicator_id_list is not a list')
        for item in indicator_id_list:
            if not isinstance(item,unicode):
                raise Exception('indicator_id_list item is not a str')
        id_list = ctrl.get_id_list()
        if not isinstance(id_list,list):
            raise Exception('id_list is not a list')
        for item in id_list:
            if not isinstance(item,unicode):
                raise Exception('id_list item is not a str')
        title_dict = ctrl.get_title_dict()
        if not isinstance(title_dict,dict):
            raise Exception('title_dict is not a dict')
        indicator_dict = ctrl.get_indicator_dict()
        if not isinstance(indicator_dict,dict):
            raise Exception('indicator_dict is not a dict')
        prefix = ctrl.get_prefix()
        self.assertEqual('wencai',prefix)

if __name__ == '__main__':
    unittest.main()


