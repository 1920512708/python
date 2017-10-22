# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 20:57:20 2017

@author: zhou
"""

from urllib import request

def downimg():
    url = "https://file.cmbchina.com/employImages/201709/4c05c0e8-6736-4594-96ea-cad1d7b35f61.png"
    rep = request.Request(url)
    rep.add_header('user-agent','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36')
    html = request.urlopen(rep)
    img = html.read()
    with open('nonghan.png', 'wb') as f:
        f.write(img)