
class IndexListCtrl(QtCore.QObject):
    def __init__(self, main_ctrl, setting):
        super(IndexListCtrl,self).__init__()
        #main_ctrl 与index_list_ctrl相互引用
        self.setting = setting
        self.main_ctrl = main_ctrl
        main_ctrl.index_list_ctrl = self
        self.index_list = self.create_index_list()
        self.connect(self.index_list,
            QtCore.SIGNAL('nth_btn_press(QString)'),
            self.on_nth_index_press)

    #响应qindex_list的第n个组件的press事件,然后紧紧是发出changed的信号,通知其他
    #控制器
    def on_nth_index_press(self,_id):
        self.emit(QtCore.SIGNAL('changed()'))

    #构造完各种东西, 就该start去初始化各view和ctrl的连接了
    def start(self):
        self.index_list.start()

    def create_index_list(self):
        setting = self.setting
        index_list = QIndexList(
            self.main_ctrl.main_window,
            setting['index_list_header'],
            setting['index_list_title'],
            setting['index_list_id'],
            setting['index_list_icon'])
        index_list.setMaximumWidth(setting['index_list_width'])
        index_list.setGeometry(*setting['index_list_geometry'])
        return index_list

    def get_current_id(self):
        return self.index_list.wrapper_id