#!/usr/bin/python  
# -*- coding: utf-8 -*-
import sys
from PyQt4 import QtGui
from PyQt4 import Qt  
from PyQt4 import QtCore  
from qlist_item import QListItem

class QIndexList(QtGui.QWidget):
    def __init__(self,parent,title,index_list,id_list,image_list):
        super(QIndexList,self).__init__(parent)
        self.title = title
        self.id_list = id_list
        self.index_list = index_list
        self.image_list = image_list
        self.button_list = []
        self.wrapper_id = id_list[0]
        self.initUI()      
        
    def initUI(self):
        self.title_label = QtGui.QLabel(self.title,self)
        self.title_label.setProperty('cls','header')
        vbox = QtGui.QVBoxLayout()
        vbox.addWidget(self.title_label)
        vbox.setSpacing(0)
        #init ui
        for i in range(len(self.index_list)):
            list_item = QListItem(self,
                                  self.index_list[i],
                                  QtGui.QPixmap(self.image_list[i]),
                                  self.id_list[i])
            self.connect(list_item,
                         QtCore.SIGNAL('clicked(QString)'),
                         self.on_nth_btn_press)
            self.button_list.append(list_item)
            vbox.addWidget(list_item)
        self.setLayout(vbox)
        self.resetStyleSheet()

    def start(self):
        self.resetStyleSheet()

    def resetStyleSheet(self):
        for i in range(len(self.index_list)):
            if self.button_list[i].id == self.wrapper_id:
                self.button_list[i].setProperty('states','selected')
            else:
                self.button_list[i].setProperty('states','unselected')
            self.button_list[i].update()
            self.button_list[i].style().unpolish(self.button_list[i])
            self.button_list[i].style().polish(self.button_list[i])

    def on_nth_btn_press(self,_id):
         self.wrapper_id = str(_id)
         self.resetStyleSheet()
         self.emit(QtCore.SIGNAL('nth_btn_press(QString)'),_id )

class Example(QtGui.QWidget):
    def __init__(self):
        super(Example,self).__init__()
        self.initUI()

    def initUI(self):
        title = u'条件设置'
        index_list = [u'基本指标',u'我的收藏']
        image_list = [
            QtGui.QImage('../images/icon_menu_stock_filter_1.png'),
            QtGui.QImage('../images/icon_menu_stock_filter_2.png')]
        self.index_list = QIndexList(self,title,index_list,image_list)
        hbox = QtGui.QHBoxLayout()
        hbox.addWidget(self.index_list)
        self.setLayout(hbox)
        self.setStyleSheet('font-size:14px')

def main():

    app = QtGui.QApplication(sys.argv)
    ex = Example()
    ex.show()
    app.exec_()


if __name__ == '__main__':
    main()