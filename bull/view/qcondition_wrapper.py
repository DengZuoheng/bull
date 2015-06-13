#!/usr/bin/python  
# -*- coding: utf-8 -*-
import sys
from PyQt4 import QtGui
from PyQt4 import Qt  
from PyQt4 import QtCore 
from qbase_wrapper import QBaseWrapper
from qid_checkbox import QIDCheckBox

class QConditionWrapper(QBaseWrapper):
    def __init__(self,wrapper_id,parent,title,title_list,id_list):
        super(QBaseWrapper, self).__init__(parent).__init__(parent)
        self.wrapper_id = wrapper_id
        self.title = title
        self.title_list = title_list
        self.id_list = id_list
        self.checkbox_list = []
        self.init_condition()
        self.init_gui()

    def init_condition(self):
        self.condition = []  

    def init_gui(self):
        self.inner_frame = QtGui.QWidget()
        inner_layout = QtGui.QFormLayout(self.inner_frame)
        inner_layout.setVerticalSpacing(10)
        for i in range(len(self.title_list)): 
            check_box = QIDCheckBox(
                self.title_list[i],
                self.inner_frame,
                self.id_list[i])

            self.connect(
                check_box,
                QtCore.SIGNAL('changed(int,QString)'),
                self.on_id_checkbox_change)
            self.checkbox_list.append(check_box)
            inner_layout.addWidget(check_box)

        scroll = QtGui.QScrollArea()
        scroll.setWidget(self.inner_frame)
        scroll.setWidgetResizable(True)
        layout = QtGui.QVBoxLayout()
        label = QtGui.QLabel(self.title)
        label.setProperty('cls','header')
        layout.addWidget(label)
        layout.addWidget(scroll)
        self.setLayout(layout)

    def get_condition(self):
        return self.condition

    def refresh_condition(self,state,_id):
        temp = [_id,None,None]
        if state == QtCore.Qt.Checked:
            if temp in self.condition:
                return 
            self.condition.append(temp)
        else:
            if temp in self.condition:
                self.condition.pop(self.condition.index(temp))

    def set_condition(self,condition):
        self.condition = condition
        self.refresh_checkbox_list()

    def refresh_checkbox_list(self):
        id_list = [item[0] for item in self.condition]
        for item in self.checkbox_list:
            if  item.id  in id_list:
                item.setCheckState(QtCore.Qt.Checked)
            else:
                item.setCheckState(QtCore.Qt.Unchecked)

    def on_id_checkbox_change(self,state,_id):
        self.refresh_condition(state,str(_id))
        self.emit(QtCore.SIGNAL('changed()'))

    def reset(self):
        self.set_condition([])

################################################################################
################################################################################
#以下测试
class Example(QtGui.QWidget):
    def __init__(self):
        super(Example,self).__init__()
        self.initUI()

    def initUI(self):
        title = u'可选条件'
        title_list = [u'总市值',u'流通市值',u'动态市盈率',u'静态市盈率']
        id_list = ['a','b','c','d']
        self.condition_wrapper = QConditionWrapper(self,title,title_list,id_list)
        self.connect(self.condition_wrapper,
                     QtCore.SIGNAL('changed()'),
                     self.onConditionWrapperChanged)
        hbox = QtGui.QHBoxLayout()
        hbox.addWidget(self.condition_wrapper)
        self.setLayout(hbox)

    def onConditionWrapperChanged(self):
        print(self.condition_wrapper.get_condition())

def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    ex.show()
    app.exec_()


if __name__ == '__main__':
    main()

