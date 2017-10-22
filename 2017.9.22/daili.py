# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 09:03:47 2017

@author: zhou
"""
from urllib import request

url = 'http://www.fishc.com'

handler = request.ProxyHandler({'http':'168.195.209.99:65205'})
opener = request.build_opener(handler)
opener.open(url)

rep = request.Request(url)
html = request.urlopen(rep)
rep = html.read().decode('utf-8')
print(rep)