# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 08:40:56 2017

@author: zhou
"""

from urllib import request

url = 'http://placekitten.com/g/300/300'

rep = request.urlopen(url)
html = rep.read()
with open('cat_1.jpg', 'wb') as f:
    f.write(html)