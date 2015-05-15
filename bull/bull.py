#!/usr/bin/python  
# -*- coding: utf-8 -*-
from PyQt4 import QtGui
from PyQt4 import Qt  
from PyQt4 import QtCore  
from view.qmainwindow import QMainWindow
from controller.setting_ctrl import SettingCtrl
from controller.qss_ctrl import QSSCtrl

if __name__ == '__main__':   
    import sys
    app = QtGui.QApplication(sys.argv)
    setting_ctrl = SettingCtrl()
    qss_ctrl = QSSCtrl()
    app.setStyleSheet(qss_ctrl.get_qss())
    main_window = QMainWindow(setting_ctrl.get_setting())
    main_window.show()
    sys.exit(app.exec_())