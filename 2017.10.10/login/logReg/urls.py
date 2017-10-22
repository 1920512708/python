from django.conf.urls import url

from logReg import views

urlpatterns = [
    url(r'^login/$', views.login,name='login'),
    url(r'^regist/$', views.regist,name='regist'),
    url(r'^index/$', views.index,name='index'),
    url(r'^logout/$', views.logout,name='logout'),
]