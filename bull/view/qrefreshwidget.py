#!/usr/bin/python  
# -*- coding: utf-8 -*-
from PyQt4 import QtGui
from PyQt4 import Qt  
from PyQt4 import QtCore 

class QRefreshWidget(QtGui.QFrame):
    def __init__(self,parent,text,gif,movie_size):
        super(QRefreshWidget,self).__init__(parent)
        self.text = text
        self.gif = gif
        self.movie = QtGui.QMovie(gif,QtCore.QByteArray(),self)
        self.movie.setScaledSize(QtCore.QSize(*movie_size))
        self.movie_screen = QtGui.QLabel(self)
        self.movie_screen.setMargin(0)
        self.movie_screen.setFixedWidth(14)
        self.movie_screen.setFixedHeight(18)
        self.movie_screen.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        self.movie_screen.setAlignment(QtCore.Qt.AlignCenter)
        main_layout = QtGui.QHBoxLayout()
        main_layout.addWidget(self.movie_screen)
        self.text_label = QtGui.QLabel(text,self)
        self.text_label.setAlignment(QtCore.Qt.AlignVCenter)
        self.text_label.setFixedHeight(18)
        main_layout.addWidget(self.text_label)
        self.setLayout(main_layout)
        self.movie.setCacheMode(QtGui.QMovie.CacheAll)
        self.movie.setSpeed(100)
        self.movie_screen.setMovie(self.movie)
        self.movie.start()
        self.movie.setPaused(True)
        self.clickable = True
        self.movie_paused = True


    def mousePressEvent(self,QMouseEvent):
        if self.clickable == True:
            self.movie_paused = False
            self.set_movie_paused()
            self.emit(QtCore.SIGNAL('clicked()'))

    def set_clickable(self,status):
        self.clickable = status

    def set_movie_paused(self):
        self.movie.setPaused(self.movie_paused)

    def set_movie_paused_status(self,status):
        self.movie_paused = status
        self.set_movie_paused()


class Example(QtGui.QWidget):
    def __init__(self):
        super(Example,self).__init__()
        self.initUI()

    def initUI(self):
        text = "Sync"
        image = None
        gif = '../images/refresh.gif'
        movie_size = (14,14)
        self.refresh_widget = QRefreshWidget(self,text,gif,movie_size)
        hbox = QtGui.QHBoxLayout()
        hbox.addWidget(self.refresh_widget)
        self.setLayout(hbox)

def main():
    import sys
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    ex.show()
    app.exec_()


if __name__ == '__main__':
    main()