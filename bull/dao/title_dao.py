#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
class TitleDao():
    def __init__(self,path = 'title.json'):
        self.path = path

    def load_title(self):
        f = open(self.path,'r')
        json_str = f.read()
        self.title = json.loads(json_str)
        f.close()
        return self.title

    def store_title(self,title):
        f = open(self.path,'w')
        f.write(json.dumps(title))
        f.close()
