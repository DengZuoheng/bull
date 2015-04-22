import os
import sys
path = sys.path[0] 
parent_path = os.path.dirname(path) 
sys.path.insert(0,(parent_path))
from sevice.spider import Spider
from sevice.wencaispider import WencaiSpider
spider = WencaiSpider('http://www.iwencai.com/stockpick')
item = []
item = spider.spider()
for item in self.save:
    print item.code
    print item.name
    print item.increase
    print item.price
    print item.pe
    print item.forcast
    print item.pbv
    print item.total
    print '\n'