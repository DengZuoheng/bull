#!/usr/bin/python  
# -*- coding: utf-8 -*-
import sys
from PyQt4 import QtGui
from PyQt4 import Qt  
from PyQt4 import QtCore 

class QIDCheckBox(QtGui.QCheckBox):
    def __init__(self,text,parent,id):
        super(QIDCheckBox,self).__init__(text,parent)
        self.id = id
        self.connect(self,
                     QtCore.SIGNAL('stateChanged(int)'),
                     self.onStateChanged)

    def onStateChanged(self,state):
        self.emit(QtCore.SIGNAL('changed(int,int)'),state,self.id)

class Example(QtGui.QWidget):
    def __init__(self):
        super(Example,self).__init__()
        self.initUI()

    def initUI(self):
        text = u'总市值'
        self.idcheckbox = QIDCheckBox(text,self,99)
        self.connect(self.idcheckbox,
                     QtCore.SIGNAL('changed(int,int)'),
                     self.onIDCheckBoxChanged)

        hbox = QtGui.QHBoxLayout()
        hbox.addWidget(self.idcheckbox)
        self.setLayout(hbox)

    def onIDCheckBoxChanged(self,state,id):
        print('state = %d id = %d '%(state,id))

def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    ex.show()
    app.exec_()


if __name__ == '__main__':
    main()
