#!/usr/bin/python  
# -*- coding: utf-8 -*-
from PyQt4 import QtGui
from PyQt4 import Qt  
from PyQt4 import QtCore  
from view.qbull_window import QBullWindow
from view.main_factory import MainFactory
from view.qicon_widget import QIconWidget
from view.qrefresh_widget import QRefreshWidget
from controller.refresh_ctrl import RefreshCtrl
from controller.wrapper_group_ctrl import WrapperGroupCtrl
from controller.screener_group_ctrl import ScreenerGroupCtrl


class QMainWindow(QBullWindow):
    def __init__(self,setting,parent=None):
        kwargs = {
            'parent':parent,
            'width':setting['main_frame_width'],
            'height':setting['main_frame_height'],
            'has_close':True,
            'has_mini':True,
            'setting':setting,
        }
        super(QMainWindow,self).__init__(**kwargs)
        self.setting = setting
        self.main_factory = MainFactory(setting)
        self.main_ctrl = self.main_factory.create_main_ctrl(self)
        self.initUI()

    def initUI(self):
        self.main_ctrl = self.main_factory.create_main_ctrl()   
        self.init_wrapper_group()
        self.init_screener_group()
        self.init_index_list()
        self.init_refresh_group()
        self.init_icon_group()  
        self.main_ctrl.start()    

    def init_icon_group(self):
        setting = self.setting
        icon = setting['icon_path']
        title_text = setting['title_text']
        icon_size = setting['icon_size']
        self.icon_widget = QIconWidget(self,title_text,icon,icon_size)
        self.icon_widget.setGeometry(*setting['icon_geomotry'])

    def init_refresh_group(self):
        setting = self.setting
        self.refresh_ctrl = RefreshCtrl(self,main_ctrl,setting)
        text = setting['refresh_text']
        gif = setting['refresh_gif']
        movie_size = setting['refresh_gif_size']
        self.refresh_widget = QRefreshWidget(self,text,gif,movie_size)
        self.refresh_widget.setGeometry(*setting['refresh_widget_geometry'])
        self.connect(self.refresh_widget,
            QtCore.SIGNAL('clicked()'),
            self.refresh_ctrl.on_refresh_start)
        self.refresh_progress_bar = QtGui.QProgressBar(self)
        self.refresh_progress_bar.setGeometry(*setting['refresh_progress_bar_geomotry'])
        #self.refresh_progress_bar.setGeometry(1,484,869,5)
        self.refresh_progress_bar.setTextVisible (False)
        self.refresh_progress_bar.setRange(0,4)
        self.refresh_progress_bar.setVisible(False)

    def init_index_list(self):
        factory = self.main_factory
        self.index_list_list = factory.create_index_list()
        args = [self.index_list,self.main_ctrl]
        self.index_list_ctrl = factory.create_index_list_ctrl(*args)

    def init_wrapper_group(self):
        self.wrapper_ctrl_list = []
        factory = self.main_factory
        for item in self.setting['wrapper_id_list']:
            wrapper_ctrl_args = [item, self.main_ctrl, self.setting]
            new_wrapper_ctrl = factory.create_wrapper_ctrl(*wrapper_ctrl_args)
            self.wrapper_ctrl_list.append(new_wrapper_ctrl)
        wrapper_group_ctrl = WrapperGroupCtrl(self.wrapper_ctrl_list,self.main_ctrl)
        self.main_ctrl.wrapper_ctrl_group = wrapper_group_ctrl

    def init_screnner_group(self):
        self.screener_ctrl_list = []
        factory = self.main_factory
        for item in self.setting['screnner_id_list']:
            screener_ctrl_args = [item, self.main_ctrl, self.setting]
            new_screener_ctrl = factory.create_screener_ctrl(*screener_ctrl_args)
            self.screnner_ctrl_list.append(new_screener_ctrl)
        screener_group_ctrl = ScreenerGroupCtrl(self.screener_ctrl_list,self.main_ctrl)
        self.main_ctrl.screener_group_ctrl = screener_group_ctrl
    
      
    