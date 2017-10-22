# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 16:38:40 2017

@author: zhou
"""

from urllib import request, parse
import json
import time

while True:
    content = input('请输入：')
    if content == 'quit':
        break
    
    url = 'http://fy.iciba.com/ajax.php?a=fy'
    data = {}
    data['f'] = 'auto'
    data['t'] = 'auto'
    data['w'] = content
    
    head = {}
    head['User-Agent'] = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36'
    data = parse.urlencode(data).encode('utf-8')
    #a = print(data)
    rep = request.Request(url, data, head)
    response = request.urlopen(rep)
    html = response.read().decode('utf-8')
    #print(type(html))
    rep = json.loads(html)
    print(rep)
    target = rep['content']['out']
    print(target)
    time.sleep(5)


