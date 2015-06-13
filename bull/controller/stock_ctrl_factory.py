
class StockCtrlFactory():
    def __init__(self,setting):
        self.setting = setting

    def create_stock_ctrl(self,stock_type):
        if stock_type == 'wencai':
            dao = WencaiDao(setting['db_path'],stock_type)
            ctrl = StockCtrl(dao,WencaiStock)
            return ctrl
        elif stock_type == 'xueqiu':
            dao = XueqiuDao(setting['db_path'],stock_type)
            ctrl = StockCtrl(dao,XueqiuStock)
            return ctrl