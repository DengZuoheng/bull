#!/usr/bin/python  
#-*-coding:utf-8-*-
import sys
from PyQt4 import QtGui
from PyQt4 import Qt  
from PyQt4 import QtCore  
from qscreeneritem import QScreenerItem


class QScreenerGroup(QtGui.QFrame):
    def __init__(self,
            parent,
            header,
            title_list,
            data_list,
            label_text_list,
            label_width_list,
            save_btn_alt,
            cancel_btn_alt,
            submit_btn_alt,
            range_btn_img,
            range_btn_img_active,
            screener_item_del_icon,
            screener_item_del_icon_active,
            ):
        super(QScreenerGroup,self).__init__(parent)
        self.header = header
        self.title_list = title_list
        self.data_list = data_list
        self.screener_list = []
        self.label_text_list = label_text_list
        self.label_width_list = label_width_list
        self.cancel_btn_alt = cancel_btn_alt
        self.save_btn_alt = save_btn_alt
        self.submit_btn_alt = submit_btn_alt
        self.range_btn_img = range_btn_img
        self.range_btn_img_active = range_btn_img_active
        self.screener_item_del_icon = screener_item_del_icon
        self.screener_item_del_icon_active = screener_item_del_icon_active
        self.length = len(title_list)
        self.initUI()

    def init_inner_frame(self):
        self.inner_frame = QtGui.QWidget(self)
        self.inner_layout = QtGui.QFormLayout(self.inner_frame)
        self.inner_layout.setVerticalSpacing(0)
        for i in range(self.length):
            kwargs = {
                'parent':self,
                'title':self.title_list[i],
                'data':self.data_list[i],
                'id':i,
                'range_btn_img':self.range_btn_img,
                'range_btn_img_active':self.range_btn_img_active,
                'del_btn_img':self.screener_item_del_icon,
                'del_btn_img_active':self.screener_item_del_icon_active,
            }
            screener_item = QScreenerItem(**kwargs)
            self.connect(screener_item,
                QtCore.SIGNAL('close(int)'),
                self.on_nth_item_close)
            self.inner_layout.addWidget(screener_item)
            screener_item.setVisible(False)
            self.screener_list.append(screener_item)

    def init_scroll_area(self):
        self.scroll = QtGui.QScrollArea(self)
        self.scroll.setWidget(self.inner_frame)
        self.scroll.setWidgetResizable(True)
        self.scroll.setObjectName('ScreenerScroll')

    def init_title(self):
        self.title_hbox = QtGui.QHBoxLayout()
        title_text = self.label_text_list
        title_width = self.label_width_list
        self.label_name = QtGui.QLabel(self)
        self.label_min = QtGui.QLabel(self)
        self.label_chart = QtGui.QLabel(self)
        self.label_max = QtGui.QLabel(self)
        self.label_clode = QtGui.QLabel(self)
        lblst = [
            self.label_name,
            self.label_min,
            self.label_chart,
            self.label_max,
            self.label_clode,
        ]
        i = 0
        for item in lblst:
            item.setText(title_text[i])
            item.setMinimumWidth(title_width[i])
            item.setProperty('cls','title')
            i = i+1
            self.title_hbox.addWidget(item)

    def init_header(self): 
        self.header_label = QtGui.QLabel(self.header)
        self.header_label.setProperty('cls','header')

    def init_button_group(self):             
        self.button_save = QtGui.QPushButton(self.save_btn_alt,self)
        self.button_cancel = QtGui.QPushButton(self.cancel_btn_alt,self)
        self.button_submit = QtGui.QPushButton(self.submit_btn_alt,self)
        self.button_hbox= QtGui.QHBoxLayout()
        self.button_hbox.addWidget(self.button_save)
        self.button_hbox.addWidget(self.button_cancel)
        self.button_hbox.addStretch()
        self.button_hbox.addWidget(self.button_submit)
        self.connect(self.button_save,
            QtCore.SIGNAL('clicked()'),
            self.on_button_save_clicked)
        self.connect(self.button_cancel,
            QtCore.SIGNAL('clicked()'),
            self.on_button_cancel_clicked)
        self.connect(self.button_submit,
            QtCore.SIGNAL('clicked()'),
            self.on_button_submit_clicked)

    def initUI(self):
        self.init_inner_frame()
        self.init_scroll_area()
        self.init_title()
        self.init_header()
        self.init_button_group()
        self.main_layout = QtGui.QVBoxLayout()
        self.main_layout.addWidget(self.header_label)
        self.main_layout.addLayout(self.title_hbox)
        self.main_layout.addWidget(self.scroll)
        self.main_layout.addLayout(self.button_hbox)
        self.setLayout(self.main_layout)

    def on_button_submit_clicked(self):
        self.emit(QtCore.SIGNAL('submit_event()'))

    def on_button_cancel_clicked(self):
        self.emit(QtCore.SIGNAL('cancel_event()'))

    def on_nth_item_close(self,id):
        self.screener_list[id].setVisible(False)
        self.emit(QtCore.SIGNAL('nth_item_close(int)'),id)

    def on_button_save_clicked(self):
        self.emit(QtCore.SIGNAL('save_event()'))

    def get_nth_value(self):
        return self.screener_list[i].get_value()

    def get_all_value(self):
        ret = []
        for item in self.screener_list:
            ret.append(item.get_value)
        return ret

    def set_nth_item_visible(self,id,flag):
        self.screener_list[id].setVisible(flag)

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
        data_list = [{'data':ret,'data_max':max_value,'data_min':min_value}]*16
        title_list = [u'市盈率']*16
        self.wid = QScreenerGroup(self,u'筛选条件',title_list,data_list)
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
