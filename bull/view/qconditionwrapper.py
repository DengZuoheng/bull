#!/usr/bin/python  
#-*-coding:utf-8-*-
import sys
from PyQt4 import QtGui
from PyQt4 import Qt  
from PyQt4 import QtCore 
from qidcheckbox import QIDCheckBox

class QConditionWrapper(QtGui.QFrame):
    def __init__(self,parent,title,title_list):
        super(QConditionWrapper,self).__init__(parent)
        self.checkbox_list = []
        self.inner_frame = QtGui.QWidget()
        inner_layout = QtGui.QFormLayout(self.inner_frame)
        inner_layout.setVerticalSpacing(10)
        for i in range(len(title_list)):
            check_box = QIDCheckBox(title_list[i],self.inner_frame,i)
            self.connect(check_box,
                         QtCore.SIGNAL('changed(int,int)'),
                         self.on_nth_checkbox_changed)
            self.checkbox_list.append(check_box)
            inner_layout.addWidget(check_box)
        scroll = QtGui.QScrollArea()
        scroll.setWidget(self.inner_frame)
        scroll.setWidgetResizable(True)
        layout = QtGui.QVBoxLayout()
        label = QtGui.QLabel(title)
        label.setProperty('cls','header')
        layout.addWidget(label)
        layout.addWidget(scroll)
        self.setLayout(layout)

    def on_nth_checkbox_changed(self,state,id):
        self.emit(QtCore.SIGNAL('nth_changed(int,int)'),state,id)

    def get_state_list(self):
        ret = []
        for i in self.checkbox_list:
            ret.append(i.checkState())
        return ret

    def get_nth_state(self,n):
        return self.checkbox_list[n].checkState()

    def set_nth_state(self,n,flag):
        if flag == True:
            self.checkbox_list[n].setCheckState(QtCore.Qt.Checked)
        else:
            self.checkbox_list[n].setCheckState(QtCore.Qt.Unchecked)

    def set_state_by_list(self,l):
        for i in range(len(l)):
            self.checkbox_list[i].setCheckState(l[i])

class Example(QtGui.QWidget):
    def __init__(self):
        super(Example,self).__init__()
        self.initUI()

    def initUI(self):
        title = u'可选条件'
        title_list = [u'总市值',u'流通市值',u'动态市盈率',u'静态市盈率']*3
        self.condition_wrapper = QConditionWrapper(self,title,title_list)
        self.connect(self.condition_wrapper,
                     QtCore.SIGNAL('changed()'),
                     self.onConditionWrapperChanged)
        hbox = QtGui.QHBoxLayout()
        hbox.addWidget(self.condition_wrapper)
        self.setLayout(hbox)

    def onConditionWrapperChanged(self):
        print(self.condition_wrapper.get_state_list())

def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    ex.show()
    app.exec_()


if __name__ == '__main__':
    main()
