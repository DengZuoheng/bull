#!/usr/bin/python  
# -*- coding: utf-8 -*-
import sys
from PyQt4 import QtGui
from PyQt4 import Qt  
from PyQt4 import QtCore 
from qfavitem import QFavItem
from qconfirm_message_box import QConfirmMessageBox
from qbase_wrapper 

class QFavWrapper(QBaseWrapper):
    def __init__(self,parent,title,fav_list,setting,delete_btn_image):
        super(QFavWrapper, self).__init__(parent)
        self.fav_list = fav_list
        self.favitem_list = []
        self.setting = setting
        self.delete_btn_image = delete_btn_image
        self.inner_frame = QtGui.QWidget()
        inner_layout = QtGui.QFormLayout(self.inner_frame)
        inner_layout.setVerticalSpacing(10)
        for item in fav_list:
            favitem = QFavItem(self,item['favid'],item['title'],
                self.delete_btn_image)
            self.connect(favitem,
                        QtCore.SIGNAL('clicked(int)'),
                        self.on_nth_click)
            self.connect(favitem,
                        QtCore.SIGNAL('closed(int)'),
                        self.on_nth_close)
            self.favitem_list.append(favitem)
            inner_layout.addWidget(favitem)
        self.inner_layout = inner_layout
        scroll = QtGui.QScrollArea()
        scroll.setWidget(self.inner_frame)
        scroll.setWidgetResizable(True)
        layout = QtGui.QVBoxLayout()
        label = QtGui.QLabel(title)
        label.setProperty('cls','header')
        layout.addWidget(label)
        layout.addWidget(scroll)
        self.setLayout(layout)

    def get_condition(self):
        for item in self.fav_list:
            if item['favid'] == self.selected_id:
                return item['condition'] 

    def set_condition(self,condition):
        for item in self.fav_list:
            if item['favid'] == self.selected_id:
                item['condition'] = condition

    def on_nth_click(self,_id):
        self.selected_id = _id
        self.emit(QtCore.SIGNAL('changed()'))

    def on_nth_close(self,_id):
        dlg_data={
            'setting':self.setting,
            'title_text':self.setting['fav_delete_dlg_title_text'],
            'main_confirm_text':self.setting['fav_delete_confirm_text'],
            'confirm_tips':self.setting['fav_delete_confirm_tips'],
        }
        dlg = QConfirmMessageBox(self,dlg_data)
        dlg.exec_()
        if dlg.get_confirm()==False:
            for item in self.favitem_list:
                item.closed = False
            return
        idx = [item['favid'] for item in self.fav_list].index(_id)
        self.favitem_list[idx].setVisible(False)
        self.inner_layout.removeWidget(self.favitem_list[idx])
        self.favitem_list.pop(idx)
        self.emit(QtCore.SIGNAL('nth_close(int)'),_id)

    def add_fav_item(self,fav):
        if fav not in self.fav_list:
            fav_list.append(fav)
        favitem = QFavItem(self,fav['favid'],fav['title'],
                self.delete_btn_image)
        self.connect(favitem,
                    QtCore.SIGNAL('clicked(int)'),
                    self.on_nth_click)
        self.connect(favitem,
                    QtCore.SIGNAL('closed(int)'),
                    self.on_nth_close)
        self.favitem_list.append(favitem)
        self.inner_layout.addWidget(favitem)
        self.update()

    def should_connect_other(self):
        return True

    def connect_other_list(self):
        #返回当前收藏的网站id, 如'xueqiu','wencai'
        #TODO
        pass


class Example(QtGui.QWidget):
    def __init__(self):
        super(Example,self).__init__()
        self.initUI()

    def initUI(self):
        title = u'可选分组'
        fav_list = [{'favid':100,'title':'100'},
            {'favid':102,'title':'102'},
            {'favid':103,'title':'103'}]
        self.fav_wrapper = QFavWrapper(self,title,fav_list)
        hbox = QtGui.QHBoxLayout()
        hbox.addWidget(self.fav_wrapper)
        self.setLayout(hbox)

def main():
    app = QtGui.QApplication(sys.argv)
    app.setStyleSheet("""
        *{
            background:white;
        }
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