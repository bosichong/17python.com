from django.conf.urls import url
from django.contrib import admin
from . import views as v #引项目的视图文件

urlpatterns = [
    url(r'^$', v.index),#项目首页
]