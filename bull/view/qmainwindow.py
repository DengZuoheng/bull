#!/usr/bin/python  
# -*- coding: utf-8 -*-
from PyQt4 import QtGui
from PyQt4 import Qt  
from PyQt4 import QtCore  
from view.qhoverbutton import QHoverButton
from view.qindexlist import QIndexList
from view.qconditionwrapper import QConditionWrapper
from view.qscreenergroup import QScreenerGroup
from controller.conditon_wrapper_ctrl import ConditionWrapperCtrl
from controller.screener_group_ctrl import ScreenerGroupCtrl

class QMainWindow(QtGui.QDialog):
    def __init__(self,setting,parent=None):
        super(QMainWindow,self).__init__(parent)
        self.setting = setting
        self.initUI()

    def initUI(self):
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint |QtCore.Qt.Dialog)
        self.setFixedWidth(self.setting['main_frame_width'])
        self.setFixedHeight(self.setting['main_frame_height'])
        self.init_close_group()    
        self.init_condition_wrapper()
        self.init_screener_group()
        self.init_index_list()

    def init_index_list(self):
        setting=self.setting
        self.index_list = QIndexList(self,
            setting['index_list_header'],
            setting['index_list_title'],
            setting['index_list_icon'])
        self.index_list.setMaximumWidth(setting['index_list_width'])
        self.index_list.setGeometry(*setting['index_list_geometry'])

    def init_condition_wrapper(self):
        setting = self.setting
        self.condition_wrapper_ctrl = ConditionWrapperCtrl(self)
        title = setting['condition_wrapper_header']
        title_list = self.condition_wrapper_ctrl.get_title_list(setting)
        title_dict = setting['condition_wrapper_title_dict']
        self.condition_wrapper = QConditionWrapper(self,title,title_list)
        self.condition_wrapper.setGeometry(*setting['condition_wrapper_geometry'])
        self.connect(self.condition_wrapper,
            QtCore.SIGNAL('nth_changed(int,int)'),self.on_nth_checkbox_change)
        self.title_list = title_list

    def init_screener_group(self):
        setting = self.setting
        self.screener_group_ctrl = ScreenerGroupCtrl(self)
        init_args = self.screener_group_ctrl.get_init_args(setting)
        self.screener_group = QScreenerGroup(self,*init_args)
        self.screener_group.setGeometry(*setting['screener_group_geometry'])
        self.connect(self.screener_group,
            QtCore.SIGNAL('nth_item_close(int)'),
            self.on_nth_screener_close)
        self.connect(self.screener_group,
            QtCore.SIGNAL('submit_event()'),
            self.screener_group_ctrl.on_submit_event)
        self.connect(self.screener_group,
            QtCore.SIGNAL('cancel_event()'),
            self.screener_group_ctrl.on_cancel_event)
        self.connect(self.screener_group,
            QtCore.SIGNAL('save_event()'),
            self.screener_group_ctrl.on_save_event)

    def init_close_group(self):
        setting = self.setting
        close_btn_image = QtGui.QImage(setting['close_btn_image_path'])
        close_btn_image_active = QtGui.QImage(setting['close_btn_image_active_path'])
        mini_btn_image = QtGui.QImage(setting['mini_btn_image_path'])
        mini_btn_image_active = QtGui.QImage(setting['mini_btn_image_active'])
        self.close_btn = QHoverButton(self,close_btn_image,close_btn_image_active)
        self.mini_btn = QHoverButton(self,mini_btn_image,mini_btn_image_active)
        self.close_btn.setGeometry(*setting['close_btn_geometry'])
        self.mini_btn.setGeometry(*setting['mini_btn_geometry'])
        self.close_btn.setToolTip(setting['close_btn_tool_tip'])
        self.mini_btn.setToolTip(setting['mini_btn_tool_tip'])
        self.connect(self.mini_btn,
                     QtCore.SIGNAL('clicked()'),
                    self.onMinimizedButtonClick)
        
        self.connect(self.close_btn,
                    QtCore.SIGNAL('clicked()'),
                    self.onCloseButtonClick)

    def on_cancel_event(self):
        pass

    def on_save_event(self):
        pass

    def on_submit_event(self):
        pass

    def on_nth_screener_close(self,id):
        self.condition_wrapper.set_nth_state(id,False)
       
    def on_nth_checkbox_change(self,state,id):
        if state == 2:
            self.screener_group.set_nth_item_visible(id,True) 
        if state == 0:
            self.screener_group.set_nth_item_visible(id,False)
      
    def onCloseButtonClick(self):
        self.close()
        
    def onMinimizedButtonClick(self):
        self.showMinimized()
         
    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.dragPosition = event.globalPos() - self.frameGeometry().topLeft()
            QtGui.QApplication.postEvent(self, QtCore.QEvent(174))
            event.accept()
 
    def mouseMoveEvent(self, event):
        if event.buttons() == QtCore.Qt.LeftButton:
            self.move(event.globalPos() - self.dragPosition)
            event.accept()