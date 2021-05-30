from django.conf.urls import url
from . import views as v #引项目的视图文件

urlpatterns = [
    url(r'^$', v.list, name=''),#项目首页
    url(r'^home$', v.home, name='home'),
    # url(r'^list$', v.list, name='list'),

    url(r'^blog/(?P<id>\w+)$', v.blog,),

    url(r'^robots\.txt$', v.robots),  # robots
    # sitemaps url设置
    url(r'^sitemap\.xml$', v.sitemap),
]