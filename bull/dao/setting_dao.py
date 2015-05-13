#!/usr/bin/python  
#-*-coding:utf-8-*-
import json
class SettingDao():
    def __init__(self,path='setting.json'):
        self.path = path

    def load_setting(self):
        f = open(self.path,'r')
        json_str = f.read()
        self.setting = json.loads(json_str)    
        f.close()    
        return self.setting

    def store_setting(self,setting):
        f = open(self.path,'w')
        f.write(json.dumps(title))
        f.close()

