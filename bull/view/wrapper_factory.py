
@singleton
class WrapperFactory(QtCore.QObject):
    def __init__(self,setting):
        self.setting = setting

    def create_wrapper(self,wrapper_id,main_window,dao=None):
        setting = self.setting
        if wrapper_id == 'wencai':#同花顺数据
            kwargs = {
                'wrapper_id': _wrapper_id,
                'parent' : main_window,
                'title' : setting['wencai_condition_warpper_title'],
                'title_list' : setting['wencai_condition_wrapper_title_list'],
                'id_list' : setting['wencai_condition_wrapper_id_list'],
            }
            condition_wrapper = QConditionWrapper(**kwargs)
        elif wrapper_id == 'xueqiu':#雪球数据
            kwargs = {
                'id': _wrapper_id,
                'parent': main_window,
                'title': setting['xueqiu_condition_wrapper_title'],
                'title_list':setting['xueqiu_condition_wrapper_title_list'],
                'id_list':setting['xueqiu_condition_wrapper_id_list'],
            }
            condition_wrapper = QConditionWrapper(**kwargs)

        elif wrapper_id == 'fav':#收藏
            kwargs = {
                'parent':main_window,
                'title':setting['fav_wrapper_header'],
                'fav_list':dao.load_fav(),
                'setting':setting,
                'delete_btn_image':QtGui.QImage(setting['close_icon_path']),
            }
            condition_wrapper = QFavWrapper(**kwargs)

        condition_wrapper.setGeometry(*setting['condition_wrapper_geometry'])
        return condition_wrapper
