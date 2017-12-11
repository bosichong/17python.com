from django.conf.urls import url
from django.contrib import admin
from . import views as v #引项目的视图文件

urlpatterns = [
    url(r'^$', v.list, name=''),#项目首页
    url(r'^home$', v.home, name='home'),
    # url(r'^list$', v.list, name='list'),

    url(r'^blog/(?P<id>\w+)$', v.blog,),
]