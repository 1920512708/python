# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 08:26:28 2017

@author: zhou
"""

from urllib import request

url = 'http://www.fishc.com'

html = request.urlopen(url)
rep = html.read().decode('utf-8')
print(rep)