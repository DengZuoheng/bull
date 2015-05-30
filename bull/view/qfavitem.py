#!/usr/bin/python  
# -*- coding: utf-8 -*-
import sys
from PyQt4 import QtGui
from PyQt4 import Qt  
from PyQt4 import QtCore 
from qhoverbutton import QHoverButton

class QFavItem(QtGui.QFrame):
    def __init__(self,parent,fav_id,title,close_btn_img):
        super(QFavItem, self).__init__(parent)
        self.fav_id = fav_id
        self.title = title.decode('utf-8')
        self.close_btn_img = close_btn_img

        self.title_label = QtGui.QLabel(self.title)
        self.close_button = QHoverButton(self,self.close_btn_img,None,9,9)
        self.close_button.setVisible(False)
        self.connect(self.close_button,
            QtCore.SIGNAL('clicked()'),
            self.on_close_btn_click)
        hbox = QtGui.QHBoxLayout()
        hbox.addWidget(self.title_label)
        hbox.addStretch()
        hbox.addWidget(self.close_button)
        self.setLayout(hbox)
        self.installEventFilter(self)
        self.setFixedHeight(34)
        self.closed = False

    def on_close_btn_click(self):
        self.closed = True
        self.emit(QtCore.SIGNAL('closed(int)'),self.fav_id)

    def eventFilter(self, qobject, qevent):
        qtype = qevent.type()
        if qtype == QtCore.QEvent.Enter:
            self.__hover = True
            self.hover()
        if qtype == QtCore.QEvent.Leave:
            self.__hover = False
            self.hover()
        if qtype == QtCore.QEvent.MouseButtonPress:
            if self.closed == False:
                self.setProperty('cls','focus')
                self.update()
                self.style().unpolish(self)
                self.style().polish(self)
                self.emit(QtCore.SIGNAL('clicked(int)'),self.fav_id)
        return super(QFavItem, self).eventFilter(qobject, qevent)

    def hover(self):
        self.close_button.setVisible(self.__hover)

    def set_title(self, new_title):
        self.title = new_title
        self.title_label.setText(new_title)

class Example(QtGui.QWidget):
    def __init__(self):
        super(Example,self).__init__()
        self.initUI()

    def initUI(self):
        title = u'收藏'
        self.fav_item = QFavItem(self,233,u'这是一个收藏',
            QtGui.QImage('../images/close_icon.png'))
        hbox = QtGui.QHBoxLayout()
        hbox.addWidget(self.fav_item)
        self.setLayout(hbox)

def main():
    app = QtGui.QApplication(sys.argv)
    app.setStyleSheet("""
        .QFavItem{
            border: 1px solid #e4f2ff;
            background-color:#f7fbff;
            border-radius: 3px;
            padding:0;
            margin:0;
        }
        """)
    ex = Example()
    ex.show()
    app.exec_()


if __name__ == '__main__':
    main()


