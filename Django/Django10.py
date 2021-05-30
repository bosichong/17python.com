#codeing=utf-8
# @Time    : 2017-12-09
# @Author  : py.sky
# @Mail    : bosichong@qq.com
# @Site    : www.17python.com
# @Title   : # 实战：利用Django开发部署自己的个人博客（10）Django上下文Context解决全站通用数据
# @Url     : http://www.17python.com/blog/62
# @Details : # 实战：利用Django开发部署自己的个人博客（10）Django上下文Context解决全站通用数据
# @Other   : OS X 10.11.6 
#            Python 3.6.1
#            VSCode 1.15.1
###################################
# 实战：利用Django开发部署自己的个人博客（10）Django上下文Context解决全站通用数据
###################################

'''
09节我们通过`Django`模板的继承对blog的两个模板页进行了改造，大大减少了模板中重复的代码，编码中复用及重构才是王道哈。

## `Django`的上下文Context

现在的blog中主要有两个模板文件，对应二个视图的函数，我们也了解到如果模板需要数据，需要从视图函数中通过`return render()`来传递。
但我们发现一个问题，就是两个模板需要一些很多相同的数据，比如两个模板中右侧都blog分类和站长资料展示，如果我们按常规操作，
每个视图函数中都需要获取一下这二个数据，然后返回，这样做显然不合适，如果有成百上千个模板页的话我们就要写千百段代码，如果需要修改，我们就要修改千百段代码。
这显然是一个坑，不过`Django`提供了一个上下文Context功能，很好的解决了这个问题。

## 创建`Django`上下文Context

`Context`实际上就是一个文件中带有一个字典返回值的函数，这样看来创建上下文Context，需要创建一个文件和一个函数，
然后还需要在配置文件中添加到配置项。

创建`myblog.blog_context.py` 编写代码如下：

    #coding=utf-8
    from django.conf import settings as original_settings#必须引入
    from myblog.models import UserProfile, Category, Siteinfo#导入一些必须的model
    def blog_info(request):
        #站长及博客上下文数据管理
        userinfo = UserProfile.objects.get(pk=1)#站长资料
        siteinfo = Siteinfo.objects.get(pk=1)#blog相关资料
        categorts = Category.objects.all().order_by('sort_id')#根据排序获取所有分类
        #把获取的数据通过字典返回
        return {'userinfo':userinfo, 'siteinfo':siteinfo, 'categorts':categorts}

在`settings.py.TEMPLATES.OPTIONS.context_processors`下添加我们刚刚创建文件的地址:

    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [],
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    'django.template.context_processors.debug',
                    'django.template.context_processors.request',
                    'django.contrib.auth.context_processors.auth',
                    'django.contrib.messages.context_processors.messages',
                    #上下文Context
                    'myblog.blog_context.blog_info'
                ],
            },
        },
    ]

好吧，你是不是要说，就这么简单？好吧，我们把获取的数据添加到模板中测试，如果你没有分类及站长资料数据，请先自己更新一些，
我们修改`base.html`中的站长的关于我：

      <section class="am-panel am-panel-default">
        <div class="am-panel-hd">关于我</div>
        <div class="am-panel-bd">
          <p>{{ userinfo.detail }}</p>
        </div>
      </section>

然后我查看`http://127.0.0.1:8000/blog/list` 和 `http://127.0.0.1:8000/blog/blog/1`

![]()

怎么样？是不是有种打了很久的游戏才通关的爽，上下文用起来真的是很方便，我在改改分类：

      <section class="am-panel am-panel-default">
        <div class="am-panel-hd">关于我</div>
        <div class="am-panel-bd">
          <p>{{ userinfo.detail }}</p>
        </div>
      </section>
      <section class="am-panel am-panel-default">
        <div class="am-panel-hd">文章目录</div>
        <ul class="am-list blog-list">
          {% for categort in categorts %}
          <li><a href="#">{{ categort.title }}</a></li>
          {% endfor %}
        </ul>
      </section>

然后刷新页面查看一下效果：

![]()

至此我们网站上的通用处，我们都可以使用Django模板继承和上下文来解决，大大减少了代码量，并且使程序的逻辑更为清楚！





'''