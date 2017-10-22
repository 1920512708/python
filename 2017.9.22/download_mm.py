# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 09:41:59 2017

@author: zhou
"""

from urllib import request
import os

def open_url(url):
    rep = request.Request(url)
    rep.add_header('user-agent','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36')
    html = request.urlopen(rep)
    target = html.read()
    return target
    
def get_pages(url):
    html = open_url(url).decode('utf-8')
    a = html.find('current-comment-page')+23
    b = html.find(']', a)
    rep = html[a:b]
    print(rep)
    return rep
    

def find_img(url):
    html = open_url(url).decode('utf-8')
    img_adds = []
        
    a = html.find('img src')
    while a != -1:
        b = html.find('.jpg', a, a+255)
        if b != -1:
            img_adds.append(html.split('/')[-1])
        else:
            b = a+9
        a = html.find('img src', b)
        
    for each in img_adds:
        print(each)

def save_page(img_rep):
    pass

def download(folder='ooxx', pages=2):
    os.mkdir(folder)
    os.chdir(folder)
    
    url = 'http://jandan.net/ooxx/'
    page_num = int(get_pages(url))
    
    for i in range(pages):
        page_num -= i
        url_page = url +'page-' + str(page_num) + '#comments'
        img_rep = find_img(url_page)
        save_page(img_rep)
    
if __name__ == '__main__':
    download()
        
    