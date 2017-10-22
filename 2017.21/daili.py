# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 20:35:16 2017

@author: zhou
"""
from urllib import request

url = 'http://www.whatismyip.com.tw'

proxy_support = request.ProxyHandler({'http':'111.155.116.247:8123'})

opener = request.build_opener(proxy_support)
opener.addheaders = [('User-Agent','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36')]
request.install_opener(opener)
rep = request.urlopen(url)
html = rep.read().decode('utf-8')
print(html)

