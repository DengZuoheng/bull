#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from PyQt4 import QtCore,QtGui

class QRangeSlider(QtGui.QWidget):
    def __init__(self,
            width,
            height,
            lbtn_image,
            lvalue = 0.0,
            rvalue = 1.0,
            rbtn_image = None,
            lbtn_image_active = None,
            lbtn_image_disabled = None,
            rbtn_image_active = None,
            rbtn_image_disabled = None,       
            has_rail = True,
            has_distribution = True,
            has_pointer = True,
            rail_height = 3,
            rail_line_color = QtGui.QColor(200,200,200),
            rail_fill_color = QtGui.QColor(255,255,255),
            rail_selected_fill_color = QtGui.QColor(123,191,255),
            distribution=[],
            distribution_color = QtGui.QColor(61,138,214),
            pointer_color = QtGui.QColor(200,200,200),
            active_pointer_color = QtGui.QColor(123,191,255)):

        super(QRangeSlider,self).__init__()
        self.width = width
        self.height = height
        
        self.lbtn_image = lbtn_image

        if(lbtn_image_active==None):
            self.lbtn_image_active = self.lbtn_image
        else:
            self.lbtn_image_active = lbtn_image_active
        if(lbtn_image_disabled==None):
            self.lbtn_image_disabled = self.lbtn_image
        else:
            self.lbtn_image_disabled = lbtn_image_disabled
        
        if(rbtn_image==None):
            self.rbtn_image = self.lbtn_image
        else:
            self.rbtn_image = rbtn_image

        if(rbtn_image==None and rbtn_image_active==None):
            self.rbtn_image_active = self.lbtn_image_active
        elif(rbtn_image_active==None):
            self.rbtn_image_active = self.rbtn_image
        else:
            self.rbtn_image_active = rbtn_image_active

        if(rbtn_image==None and rbtn_image_disabled==None):
            self.rbtn_image_disabled = self.lbtn_image_disabled
        elif(rbtn_image_disabled==None):
            self.rbtn_image_disabled = self.rbtn_image
        else:
            self.rbtn_image_disabled = rbtn_image_disabled

        self.has_rail = has_rail
        self.has_distribution = has_distribution
        self.has_pointer = has_pointer
        self.rail_height = rail_height
        self.rail_line_color = rail_line_color
        self.rail_fill_color = rail_fill_color
        self.rail_selected_fill_color = rail_selected_fill_color
        self.distribution = distribution
        self.distribution_color = distribution_color
        self.pointer_color = pointer_color
        self.active_pointer_color = active_pointer_color

        self.lvalue = lvalue
        self.rvalue = rvalue

        self.btn_left_press = False
        self.btn_right_press = False

        self._lw = self.lbtn_image.width()
        self._lh = self.lbtn_image.height()
        self._rw = self.rbtn_image.width()
        self._rh = self.rbtn_image.height()

        self.__calposx_by_value()
        self.__initUI()

    def __initUI(self):
        self.setMinimumSize(self.width,self.height)
        self.setMouseTracking(True)
        pass

    def __calposx_by_value(self):
        self.lposx = int(self.width*self.lvalue)
        self.rposx = self._lw+int((self.width - self._rw -self._lw)*self.rvalue)

    def __calvalue_by_posx(self):
        _lm = float(self.lposx)
        _ld = float(self.width - self._rw - self._lw)
        _rm = float(self.rposx - self._lw)
        _rd = float(self.width - self._rw - self._lw)
        self.lvalue = _lm / _ld
        self.rvalue = _rm / _rd

    def setValue(self, lvalue, rvalue):
        self.lvalue = lvalue
        self.rvalue = rvalue
        self.__calposx_by_value()
        self.update()

    def paintEvent(self,e):
        painter = QtGui.QPainter()
        painter.begin(self)
        self.__drawWidget(painter)
        painter.end()

    def __drawRail(self,painter):
        _recty = int(self.height/2)-2
        rec_pen = QtGui.QPen(self.rail_line_color)
        rec_brush = QtGui.QBrush(self.rail_fill_color)
        rec_brush_selected = QtGui.QBrush(self.rail_selected_fill_color)
        painter.setPen(rec_pen)
        painter.setBrush(rec_brush) 

        painter.drawRect(
            0,
            _recty, 
            self.lposx, 
            self.rail_height) 
        
        painter.drawRect(
            self.rposx, 
            _recty, 
            self.width - self.rposx, 
            self.rail_height)
        
        painter.setBrush(rec_brush_selected)
        
        painter.drawRect(
            self.lposx, 
            _recty, 
            self.rposx - self.lposx, 
            self.rail_height)


    def __drawBtn(self,painter):
        _lh = int(self.height/2) - self._lh/2 
        _rh = int(self.height/2) - self._rh/2 
        if(self.btn_left_press):
            painter.drawImage(
                QtCore.QPoint(self.lposx, _lh),
                self.lbtn_image_active)
        else:
            painter.drawImage(
                QtCore.QPoint(self.lposx, _lh),
                self.lbtn_image)

        if(self.btn_right_press):
            painter.drawImage(
                QtCore.QPoint(self.rposx, _rh),
                self.rbtn_image_active)
        else:
            painter.drawImage(
                QtCore.QPoint(self.rposx, _rh),
                self.rbtn_image)

    def __drawDistribution(self,painter):
        if(not self.distribution):
            return None
        active_pen = QtGui.QPen(self.distribution_color)
        painter.setPen(active_pen)
       
        _len = self.width - self._lw - self._rw
        _max = float(max(self.distribution))
        for i in range(_len):
            index = int((float(i)/_len)*len(self.distribution))+1
            h = int(self.height*(float(self.distribution[index])/_max))
            y = self.height - h
            x = self._lw + i
            painter.drawLine(x, y-1, x, self.height-1)

    def __drawPointer(self,painter):
        pen  = QtGui.QPen(self.pointer_color)
        active_pen = QtGui.QPen(self.active_pointer_color)
        lx = self.lposx + self._lw -1
        rx = self.rposx
        if(self.btn_left_press):      
            painter.setPen(active_pen)
        else:
            painter.setPen(pen)
        painter.drawLine(lx, 0, lx, self.height)

        if(self.btn_right_press):      
            painter.setPen(active_pen)
        else:
            painter.setPen(pen)
        painter.drawLine(rx, 0, rx, self.height)

    def __drawWidget(self,painter):
        if(self.has_distribution):
            self.__drawDistribution(painter)
        if(self.has_rail):
            self.__drawRail(painter)
        if(self.has_pointer):
            self.__drawPointer(painter)
        self.__drawBtn(painter) 

    def mousePressEvent(self, event):
        p = QtCore.QPointF(event.pos())

        if(self.__in_rbtn_area(p)):
            self.btn_right_press = True
            self.btn_left_press = False
            self.__mousep = p
        if(self.__in_lbtn_area(p)):
            self.btn_right_press = False
            self.btn_left_press = True
            self.__mousep = p
        self.update()
        event = QtGui.QFocusEvent(
            QtCore.QEvent.FocusIn,
            QtCore.Qt.MouseFocusReason)
        self.emit(QtCore.SIGNAL('focusIn(QFocusEvent)'),event)

    def __btn_press(self):
        if self.btn_left_press or self.btn_right_press:
            return True
        else:
            return False

    def __in_btn_area(self,point):
        if self.__in_lbtn_area(point) or self.__in_rbtn_area(point):
            return True
        else:
            return False

    def __in_lbtn_area(self, point):
        if(self.lposx <= point.x() <= self.lposx + self._lw):
            _lb = self.height/2 - self._lh/2 -1 #左边界
            _rb = self.height/2 + self._lh/2 +1 #右边界
            if(_lb <= point.y() <= _rb):
                return True
        return False

    def __in_rbtn_area(self, point):
        if(self.rposx <= point.x() <= self.rposx + self._rw):
            _lb = self.height/2 - self._rh/2 -1 
            _rb = self.height/2 + self._rh/2 +1
            if(_lb<=point.y()<=_rb):
                return True
        return False

    def __lbtn_move(self,p):
        if(p.x() <= 0):
            self.lposx = 0
        elif(p.x() + self._lw <= self.rposx):
            self.lposx = p.x()
        elif(p.x() + self._lw >= self.width - self._rw):
            self.lposx = self.width - self._rw - self._lw
            self.rposx = self.width - self._rw
        else:
            self.lposx = p.x()
            self.rposx = p.x() + self._lw

    def __rbtn_move(self,p):
        if(p.x() >= self.width - self._rw):
            self.rposx = self.width - self._rw
        elif(self.lposx +self._lw <= p.x() <=self.width):
            #还没碰到左边的
            self.rposx = p.x()
        elif(self._lw <= p.x() <= self.lposx+ self._lw ):
            #碰到了左边
            self.lposx = p.x() - self._lw
            self.rposx = p.x()
        else:
            self.lposx = 0
            self.rposx = self._lw

    def mouseMoveEvent(self, event):
        p = QtCore.QPointF(event.pos())
        if self.__in_btn_area(p) or self.__btn_press():
            self.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        else:
            self.unsetCursor()

        if(self.btn_left_press):
            new_x = self.lposx - (self.__mousep.x() - p.x())
            new_p = QtCore.QPoint(new_x, p.y())
            self.__lbtn_move(new_p)
            self.__mousep = p         
        elif(self.btn_right_press):
            new_x = self.rposx - (self.__mousep.x() - p.x())
            new_p = QtCore.QPoint(new_x, p.y())
            self.__rbtn_move(new_p)
            self.__mousep = p      
            
        self.update()
        if(self.btn_left_press or self.btn_right_press):
            self.__calvalue_by_posx()
            self.emit(QtCore.SIGNAL('valueChanged(float,float)'),
                self.lvalue,
                self.rvalue)

    def mouseReleaseEvent(self, event):
        self.btn_right_press = False
        self.btn_left_press = False
        self.update()

class Example(QtGui.QWidget):

    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):

        dis = [1,2,3,3,4,4,5,6,7,8,9,18,27,36,45,72,32,22,12,1]

        self.wid = QRangeSlider(
            width=100,
            height=30,
            distribution = dis,
            lvalue = 0.5,
            rvalue = 0.6,
            lbtn_image=QtGui.QImage('../images/drag_btn.png'),
            lbtn_image_active=QtGui.QImage('../images/drag_btn_active.png'))

        self.connect(self.wid, QtCore.SIGNAL('valueChanged(float,float)'),
            self.changeValue)
        hbox = QtGui.QHBoxLayout()
        hbox.addWidget(self.wid)
        self.setLayout(hbox)

        self.setGeometry(300, 300, 120, 40)
        self.setWindowTitle('QRangeSlider')

    def changeValue(self, lvalue,rvalue):
        print("exmaple::changeValue::value(%f,%f)"%(lvalue,rvalue))



def main():

    app = QtGui.QApplication(sys.argv)
    ex = Example()
    ex.show()
    app.exec_()


if __name__ == '__main__':
    main()