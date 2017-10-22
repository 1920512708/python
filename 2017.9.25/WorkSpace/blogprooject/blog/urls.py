# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 10:00:46 2017

@author: zhou
"""


from django.conf.urls import url
from . import views

urlpatterns = [url(r'^$', views.index, name='index'), 
               ]

