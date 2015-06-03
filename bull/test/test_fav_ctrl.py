#!/usr/bin/python  
# -*- coding: utf-8 -*-
import os
import sys
path = sys.path[0] 
parent_path = os.path.dirname(path) 
sys.path.insert(0,(parent_path))
import unittest
from controller.fav_ctrl import FavCtrl

#一个收藏数据访问对象(dao)的mockup
class fav_dao_mockup():
    def __init__(self):
        self.fav_list = [
            {
                u"favid":0,
                u"title":u"我的收藏",
                u"condition":[[u"pe",0,5],[u"peg",3,200]]
            },
            {
                u"favid":1,
                u"title":u"不知道谁的收藏",
                u"condition":[[u"pe",2,6],[u"peg",20,30],[u"pbv",55,99]]
            }
        ]
        
    def load_fav(self):
        return self.fav_list

    def store_fav(self,fav):
        self.fav_list = fav

#测试收藏控制器(fav_ctrl)
class Test_test_fav_ctrl(unittest.TestCase):
    def test_FavCtrl(self):
        dao = fav_dao_mockup()
        fav_ctrl = FavCtrl(self,dao=dao)
        fav_ctrl.set_fav(0,[])
        fav = fav_ctrl.find_fav_by_id(0)
        self.assertEqual(fav['condition'],[])
        fav_ctrl.delete_fav_by_id(0)
        self.assertEqual(len(fav_ctrl.fav_list),1)
        #new_fav已经与GUI耦合了, 测试将无法验证view类产生的BUG
        fav_ctrl.new_fav('abcd',[])
        print(fav_ctrl.fav_list)
        fav = fav_ctrl.find_fav_by_id(2)
        self.assertEqual('abcd',fav['title'])
        self.assertEqual(2,fav_ctrl.find_max_id()-1)
        fav_ctrl.set_fav(2,[[u"pe",2,6],[u"peg",20,30],[u"pbv",55,99]])
        self.assertEqual([[u"pe",2,6],[u"peg",20,30],[u"pbv",55,99]],
                         fav_ctrl.find_fav_by_id(2)['condition'])
        

if __name__ == '__main__':
    unittest.main()
