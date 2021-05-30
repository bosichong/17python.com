"""blog01 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from blog01.settings import MEDIA_ROOT
from django.views.static import serve

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^blog/', include('myblog.urls',namespace='blog')),
    url(r'^', include('myblog.urls',namespace='')),#修改为直接为域名根目录，缩短网址。

    #配置上传文件的访问处理函数
    # 需要引入
    # from MyBlog.settings import MEDIA_ROOT
    # from django.views.static import serve
    url(r'^media/(?P<path>.*)$',  serve, {"document_root":MEDIA_ROOT}, name='media'),
]
