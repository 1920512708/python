# -*- coding: utf-8 -*-
"""
Created on Sun Sep 24 14:33:28 2017

@author: zhou
"""

from urllib import request

url = 'http://jandan.net/ooxx/'

def open_url(url):
    res = request.Request(url)
    res.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36')
    rep = request.urlopen(res)
    html = rep.read()
    return html
    
def get_img(url):
    list = []
    html = open_url(url).decode('utf-8')
    a = html.find('img src')
    
    while a !=-1:
        b = html.find('.jpg', a, a+255)
        if b!=-1:
            htp = 'http:' + html[a+9:b+4]
            list.append(htp)
        else:
            b = a + 9
        a = html.find('img src', b)
    return list
    
    
def get_page(url):
    html = open_url(url).decode('utf-8')
    a = html.find('current-comment-page') + 23
    b = html.find(']', a)
    return html[a:b]
    
def save_img(img_url, filename='ooxx'):
    for i in img_url:
        html = open_url(i)
        with open(i.split('/')[-1], 'wb') as f:
            f.write(html)
            
def download_mm(url, page=2):
    
    page_num = int(get_page(url))
    
    for i in range(page):
        page_num -= i
        url1 = url + 'page-' + str(page_num) + '#comments'
        img_url = get_img(url1)
        save_img(img_url)
        
if __name__ == '__main__':
    download_mm(url)
   
    
    
    
    