#codeing=utf-8
# @Time    : 2017-11-08
# @Author  : J.sky
# @Mail    : bosichong@qq.com
# @Site    : www.17python.com
# @Title   : 实战：利用Django开发部署自己的个人博客（2）视图/路由
# @Url     : http://www.17python.com/blog/53
# @Details : 实战：利用Django开发部署自己的个人博客（2）视图/路由
# @Other   : OS X 10.11.6 
#            Python 3.6.1
#            VSCode 1.15.1
###################################
# 实战：利用Django开发部署自己的个人博客（2）视图/路由
###################################
'''
`Django`的强大之处上节我们已经体验过了，虽然上线部署还有一段距离，但一个好的开始就是预示成功即将到来。。。

## `Django`的配置文件

`blog01.settings.py`是你的项目配置文件，这里可以配置的网站常用的选项。

+ `BASE_DIR` 表示当前网站的根目录，当然你也可以添加并设置其它目录的常量
+ `DEBUG=True`的时候是开发模式，当上线部署在生产模式时这里应该设置为False
+ `INSTALLED_APPS` 这里设置你建好并启用的app 比如添加我们创建的`'myblog',`，直接添加到后边即可，记得那个逗号。
+ `MIDDLEWARE Django`中需要的模块，如果需要Django新功能模块，需要在这里添加。
+ `ROOT_URLCONF = 'blog01.urls'` 这个表示一个默认的路由，可以在这里设置一些路由的跳转
+ `DATABASES` 设置数据库，这里我们使用默认的数据库`sqlite3`即可。

还有一些其它设置项，我们会在后边用到的时候介绍，另外你也可以参考官方网站的相关文档。

我们先设置一下项目配置文件，启用新项目myblog:
`INSTALLED_APPS` 这里设置你建好并启用的app 比如添加我们创建的`'myblog',`，直接添加到后边即可，记得那个逗号。

![配图]()

接下来我们就可以设置路由

## 配置路由

路由是什么东东？假设你有一个网站域名`17python.com`,在主域名下的/blog或/news是单独一个app，
这时你就可以使用路由，单独指向自己的空间方便区分。设置我们的blog路由：
在`blog01/urls.py`中设置如下代码：


    from django.conf.urls import url, include
    from django.contrib import admin
    urlpatterns = [
        url(r'^admin/', admin.site.urls),
        url(r'^blog/', include('myblog.urls')),
    ]

这样设置路由就是把blog/下边的路由都交给`myblog.usrs.py`中来设置了。我们继续设置一个视图，验证一下我们的路由是否成功

## 编写视图
视图与路由是对好兄弟，一般都是相互存在的。我们来设置一下`blog`的主页。
先编写`myblog.views.py`中视图代码：


    from django.http import HttpResponse, HttpResponseRedirect
    def index(request):
        return HttpResponse('你好，Django,江哥？')

设置`myblog.urls.py`中的路:

    urlpatterns = [
        url(r'^$', v.index),#项目首页
        ]

设置到这里，我们就可以启动服务器测试了,还记得服务器启动命令不？

    python3 manage.py runserver

![]()

如果显示和上图一样的话，那么恭喜你！配置成功！


'''