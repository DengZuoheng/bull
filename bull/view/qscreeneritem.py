#!/usr/bin/python  
# -*- coding: utf-8 -*-
import sys
from PyQt4 import QtGui
from PyQt4 import Qt  
from PyQt4 import QtCore  
from qdistributionslider import QDistributionSlider
from qhoverbutton import QHoverButton

class QScreenerItem(QtGui.QFrame):
    def __init__(self,parent,title,data,id,
        range_btn_img,
        range_btn_img_active,
        del_btn_img,
        del_btn_img_active):
        super(QScreenerItem,self).__init__(parent)
        self.title = title
        self.data = data
        self.id = id
        self.range_btn_img = range_btn_img
        self.range_btn_img_active = range_btn_img_active
        self.del_btn_img = del_btn_img
        self.del_btn_img_active = del_btn_img_active
        self.initUI()

    def initUI(self):
        self.label = QtGui.QLabel(self.title,self)
        self.label.setFixedWidth(100)
        self.label.setFixedHeight(30)
        kwargs ={ 
            'data':self.data['data'],
            'data_max':self.data['data_max'],
            'data_min':self.data['data_min'],
            'btn_img':self.range_btn_img,
            'btn_img_active':self.range_btn_img_active
        }
        self.distribution_slider = QDistributionSlider(**kwargs)
        self.delete_button = QHoverButton(
            self,self.del_btn_img,self.del_btn_img_active)
        self.layout = QtGui.QHBoxLayout(self)
        
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.distribution_slider)
        self.layout.addWidget(self.delete_button)

        self.connect(self.delete_button,
            QtCore.SIGNAL('clicked()'),
            self.on_delete_btn_press)
        self.setFixedWidth(500)
        self.setFixedHeight(40)

    def on_delete_btn_press(self):
        self.emit(QtCore.SIGNAL('close(int)'),self.id)

    def get_value(self):
        return self.distribution_slider.get_value()

    def set_value(self,lvalue,rvalue):
        self.distribution_slider.set_value(lvalue,rvalue)

    def reset(self):
        self.distribution_slider.reset()


class Example(QtGui.QWidget):
    def __init__(self):
        super(Example,self).__init__()
        self.initUI()

    def initUI(self):
        ret = [1,4,6,4,2,5,9,4,9]
        max_value = max(ret)
        min_value = min(ret)
        data = {
            'data':ret,
            'data_max':max_value,
            'data_min':min_value,
        }
        self.wid = QScreenerItem(self,u'测试',data,99)
        hbox = QtGui.QHBoxLayout()
        hbox.addWidget(self.wid)
        self.setLayout(hbox)
        self.setWindowTitle('QScreenerItem')
        self.setStyleSheet('background:#fff;')

def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    ex.show()
    app.exec_()

if __name__=='__main__':
    main()
