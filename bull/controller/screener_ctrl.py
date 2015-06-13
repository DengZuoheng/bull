
class ScreenerCtrl(QtCore.QObject):
    def __init__(self,screener_id,main_ctrl,setting):
        super(ScreenerCtrl, self).__init__()
        self.setting = setting
        self.screener_id = screener_id
        self.main_ctrl = main_ctrl
        stock_ctrl_factory = StockCtrlFactory(setting)
        self.stock_ctrl = stock_ctrl_factory.create_stock_ctrl(screener_id)
        title_ctrl_factory = TitleCtrlFactory(setting)
        self.title_ctrl = title_ctrl_factory.create_title_ctrl(screener_id)
        screener_factory = ScreenerFactory(setting)
        screener_kwargs = {
            'main_window':main_ctrl.main_window,
            'screener_id':screener_id,
            'stock_ctrl':self.stock_ctrl,
            'title_ctrl':self.title_ctrl,
        }
        self.screener = screener_factory.create_screener(**screener_kwargs)
        #响应screener的save消息
        self.connect(self.screener,
            QtCore.SIGNAL('save_event()'),
            self.on_save_event)
        #响应screener的submit消息
        self.connect(self.screener,
            QtCore.SIGNAL('submit_event()'),
            self.on_submit_event)
        #响应screener的cancel消息
        self.connect(self.screener,
            QtCore.SIGNAL('cancel_event()'),
            self.on_cancel_event)
        #响应screener的item被关闭消息
        self.connect(self.screener,
            QtCore.SIGNAL('item_close(QString)'),
            self.on_item_close)

    def set_screener_visible(self,status):
        self.screener.setVisible(status)

    def get_condition(self):
        condition = []
        for item in self.screener.screener_item_list:
            if item.visible():
                ret = item.get_value()
                tu = (item.id,ret[0],ret[1])
                condition.append(tu)
        return condition

    def set_condition(self,condition):
        id_list = [item[0] for item in condition]
        for item in self.screener.screener_item_list:
            if item.id in id_list:
                temp = condition[id_list.index(item.id)]
                item.set_value(temp[1],temp[2])
                item.visible(True)
                item.setVisible(True)
            else:
                item.setVisible(False)

     def on_submit_event(self):
        condition = self.get_condition()
        result = self.stock_ctrl.filter(condition)
        dlg_data = {
            'header':self.setting['result_header'],
            'data':result,
            'index_map':self.setting['result_index_map'],
            'row':len(result),#行
            'col':len(self.setting['result_header']),#列
            'color':self.setting['result_color'],
            'setting':self.setting,
        }
        dlg = QResultDialog(self.view,dlg_data)
        dlg.exec_()

    def on_cancel_event(self):
        self.emit(QtCore.SIGNAL('cancel_event()'))

    def on_save_event(self):
        self.emit(QtCore.SIGNAL('save_event()'))

    def on_item_close(self):
        self.emit(QtCore.SIGNAL('changed()'))

    def update_data(self):
        data_list = self.get_data_list(self.setting)
        self.view.screener_group.update_data_list(data_list)


