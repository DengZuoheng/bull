#!/usr/bin/env python
# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod

class StockDao(object):
    def __init__(self):
        pass

    #按条件查找, 参数是一个列表, 列表的元素是一个元组
    #元组包含3项: 属性名, 最小值, 最大值
    @abstractmethod
    def filter(self,condition):
        pass

    #更新数据, stocks是一个stock models的list
    @abstractmethod
    def update(self,stocks):
        pass

