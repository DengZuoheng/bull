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
        val = 10
        inner_frame = QtGui.QWidget()
        inner_layout = QtGui.QVBoxLayout(inner_frame)
        for i in range(len(title_list)):
            check_box = QIDCheckBox(title_list[i],inner_frame,i)
            self.connect(check_box,
                         QtCore.SIGNAL('changed(int,int)'),
                         self.on_nth_checkbox_changed)
            self.checkbox_list.append(check_box)
            inner_layout.addWidget(check_box)

        scroll = QtGui.QScrollArea()
        scroll.setWidget(inner_frame)
        scroll.setWidgetResizable(True)
        #scroll.setFixedHeight(400)
        self.setStyleSheet("""
            QScrollBar:horizontal {
                 border: 1px solid grey;
                 background: white;
                height:8px;
                margin: 0;
            }
            QScrollBar::handle:horizontal {
                background: grey;
                min-width: 10px;
            }
            QScrollBar::handle:horizontal:hover {
                background: #0066cc;
                min-width: 10px;
            }
            QScrollBar::add-line:horizontal {
                border: 2px solid grey;
                background: #32CC99;
                width: 20px;
                subcontrol-position: right;
                subcontrol-origin: margin;
            }

            QScrollBar::sub-line:horizontal {
                border: 2px solid grey;
                background: #32CC99;
                width: 20px;
                subcontrol-position: left;
                subcontrol-origin: margin;
            }

            QScrollBar:vertical{
                 border: 1px solid grey;
                 background: white;
                 width: 8px;
                 margin: 0;
             }
             
             QScrollBar::handle:vertical {
                 background: grey;
                 min-height: 20px;
             }
             QScrollBar::handle:vertical:hover {
                 background: #0066cc;
                 min-height: 20px;
             }
             QScrollBar::add-line:vertical {
                 border: 0px solid grey;
                 background: #32CC99;
                 height: 0;
                 subcontrol-position: bottom;
                 subcontrol-origin: margin;
             }

             QScrollBar::sub-line:vertical {
                 border: 0px solid grey;
                 background: #32CC99;
                 height: 0;
                 subcontrol-position: top;
                 subcontrol-origin: margin;
             }
             QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {
                 border: 0px solid grey;
                 width: 3px;
                 height: 0;
                 background: red;
             }

             QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
                 background: none;
             }
            """)
        scroll.setStyleSheet('border:none')
        layout = QtGui.QVBoxLayout()
        label = QtGui.QLabel(title)
        label.setStyleSheet('font-weight:bold;padding-left:5px;padding-bottom: 20px')
        layout.addWidget(label)
        layout.addWidget(scroll)
        self.setLayout(layout)


    def on_nth_checkbox_changed(self,state,id):
        self.emit(QtCore.SIGNAL('changed()'))

    def get_state_list(self):
        ret = []
        for i in self.checkbox_list:
            ret.append(i.checkState())
        return ret

    def get_nth_state(self,n):
        return self.checkbox_list[n].checkState()

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
