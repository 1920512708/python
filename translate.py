# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 08:46:37 2017

@author: zhou
"""

from urllib import request, parse

url = 'http://fanyi.baidu.com/langdetect'

data = {}
data['query'] = 'i love fish.com'

data = parse.urlencode(data).encode('utf-8')
head = {}
head['User-Agent'] = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36'
rep = request.Request(url, data, head)
html = request.urlopen(rep)
target = html.read().decode('utf-8')
print(target)


