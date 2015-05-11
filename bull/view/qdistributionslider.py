#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from PyQt4 import QtCore,QtGui
from qrangeslider import QRangeSlider

class QDistributionSlider(QtGui.QFrame):
    def __init__(self,
            data,
            data_max,
            data_min,
            range_slider_width = 160,
            line_edit_width = 80,
            width = 335,
            height = 30,
            lvalue = 0.0,
            rvalue = 1.0):
        super(QDistributionSlider,self).__init__()
        self.width = width
        self.height = height
        self.lvalue = lvalue
        self.rvalue = rvalue
        self.data = data
        self.data_max = data_max
        self.data_min = data_min
        self.range_slider_width = range_slider_width
        self.line_edit_width = line_edit_width
        self.__initUI()

    def __uniformization(self):
        dis = [0]*(self.range_slider_width+1)
        e = float((self.data_max - self.data_min))/self.range_slider_width
        for i in self.data:
            idx = int((i-self.data_min)/e)
            dis[idx] = dis[idx]+1
        max_value = max(dis)
        for i in range(len(dis)):
            dis[i] = float(float(dis[i])/max_value)
        return dis

    def __initUI(self):
        self.setFixedSize(self.width,self.height)
        dis = self.__uniformization()
        self.range_slider = QRangeSlider(
            width=self.range_slider_width,
            height=self.height,
            distribution = dis,
            lvalue = self.lvalue,
            rvalue = self.rvalue,
            lbtn_image=QtGui.QImage('c:/Projects/bull/bull/images/drag_btn.png'),
            lbtn_image_active=QtGui.QImage('c:/Projects/bull/bull/images/drag_btn_active.png'))
        
        self.left_edit = QtGui.QLineEdit(self)
        self.left_edit.setFixedWidth(self.line_edit_width)
        self.left_edit.setFixedHeight(self.height)
        self.left_edit.setAlignment(QtCore.Qt.AlignCenter)
        
        self.right_edit = QtGui.QLineEdit(self)
        self.right_edit.setFixedWidth(self.line_edit_width)
        self.right_edit.setFixedHeight(self.height)
        self.right_edit.setAlignment(QtCore.Qt.AlignCenter)

        regexp = QtCore.QRegExp('^[0-9]*\.[0-9]*$')
        validator = QtGui.QRegExpValidator(regexp)
        self.left_edit.setValidator(validator)
        self.right_edit.setValidator(validator)
        self.__set_text(0,1)
        hbox = QtGui.QHBoxLayout()
        hbox.setContentsMargins(0, 0, 0, 0)
        hbox.addWidget(self.left_edit)
        hbox.addWidget(self.range_slider)
        hbox.addWidget(self.right_edit)
        self.setLayout(hbox)
        self.connect(self.range_slider,
            QtCore.SIGNAL('focusIn(QFocusEvent)'),
            self.range_slider_focused)
        self.connect(self.range_slider, 
            QtCore.SIGNAL('valueChanged(float,float)'),
            self.changeRange)
        self.connect(self.left_edit,
            QtCore.SIGNAL('textEdited(const QString&)'),
            self.left_edit_press)
        self.connect(self.right_edit,
            QtCore.SIGNAL('textEdited(const QString&)'),
            self.right_edit_press)

    def left_edit_press(self, qstr):
        if(qstr==''):
            self.lvalue = 0
        else:
            self.lvalue = float(qstr)
        if(self.lvalue>self.rvalue):
            if(self.lvalue>=1):
                self.lvalue = 1
            self.rvalue = self.lvalue
        self.range_slider.setValue(self.lvalue,self.rvalue)

    def right_edit_press(self, qstr):
        if(qstr==''):
            self.rvalue = 0
        else:
            self.rvalue = float(qstr)
        if(self.rvalue<self.lvalue):
            if(self.rvalue<=0):
                self.rvalue = 0
            self.lvalue = self.rvalue
        self.range_slider.setValue(self.lvalue,self.rvalue)

    def range_slider_focused(self):
        self.left_edit.clearFocus()
        self.right_edit.clearFocus()

    def changeRange(self,lvalue,rvalue):
        self.__set_text(lvalue,rvalue)

    def __set_text(self,lvalue,rvalue):
        _left_text = lvalue*(self.data_max-self.data_min)+self.data_min
        _right_text = rvalue*(self.data_max-self.data_min)+self.data_min
        self.left_edit.setText('%f'%_left_text)
        self.right_edit.setText('%f'%_right_text)



class Example(QtGui.QWidget):
    def __init__(self):
        super(Example,self).__init__()
        self.initUI()

    def initUI(self):
        ret = [1,4,6,4,2,5,9,4,9]
        max_value = max(ret)
        min_value = min(ret)
        self.wid = QDistributionSlider(ret,max_value,min_value)
        hbox = QtGui.QHBoxLayout()
        hbox.addWidget(self.wid)
        self.setLayout(hbox)
        self.setGeometry(300, 300, 200, 40)
        self.setWindowTitle('QDistributionSlider')

def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    ex.show()
    app.exec_()

if __name__=='__main__':
    main()




