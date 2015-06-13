#!/usr/bin/python  
# -*- coding: utf-8 -*-
from wencai_refresh_thread import WencaiRefreshThread
from xueqiu_refresh_thread import XueqiuRefreshThread

class RefreshThreadFactory():
    def __init__(self,setting):
        self.setting = setting

    def create_refresh_thread(self,screener_id,ctrl):
        setting = self.setting
        if screener_id == 'wencai':
            return WencaiRefreshThread(screener_id,ctrl,setting)
        elif screener_id == 'xueqiu':
            return XueqiuRefreshThread(screener_id,ctrl,setting)
