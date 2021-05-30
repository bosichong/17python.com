#codeing=utf-8
# @Time    : 2017-11-20
# @Author  : J.sky
# @Mail    : bosichong@qq.com
# @Site    : www.17python.com
# @Title   : # 实战：利用Django开发部署自己的个人博客（5）Django admin后台管理
# @Url     : http://www.17python.com/blog/57
# @Details : # 实战：利用Django开发部署自己的个人博客（5）Django admin后台管理
# @Other   : OS X 10.11.6 
#            Python 3.6.1
#            VSCode 1.15.1
###################################
# 实战：利用Django开发部署自己的个人博客（5）Django admin后台管理
###################################

'''

上节我们有数据库及表，但通过`Django shell` 来操作数据库并不太方便，而且我们是要做一个`blog`,那么我们能不能快速的拥有一个后台管理系统呢？
答案是肯定的，`Django`提供了一个功能强大的配置起来还算简单的后台管理系统，那么我们先实现这个管理系统，然后再完善一下我们的数据库及表。

## 先创建一个管理员ID

如果不创建管理员ID，在某些地方调用User表时都会多少有些问题，所以我们先创建管理员，
终端下输入：`python manage.py createsuperuser`

    ➜  blog01 git:(master) ✗ python3 manage.py createsuperuser  

    You have 2 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): myblog.
    Run 'python manage.py migrate' to apply them.

    Username (leave blank to use 'j_sky'): bosi
    Email address: bosichong@qq.com
    Password: 
    Password (again): 
    This password is too short. It must contain at least 8 characters.
    This password is entirely numeric.
    Password: 
    Password (again): 
    Superuser created successfully.

中间需要设置一个邮箱及密码，密码要求为8位以上，通过以上设置，管理员就创建成功了。

## 启用`admin`后台管理

然后我们启动服务器：`python3 manage.py runserver `
访问地址：`127.0.0.1:8000/admin/`,你会发现一个后台登陆管理系统的入口。

![]()

用刚才创建的管理员登陆，成功后如下图：

![]()

我们发现这里默认有一个用户和组的管理，没有我们的文章管理，我们来添加
编辑`myblog.admin.py`

    from django.contrib import admin
    from .models import Article

    admin.site.register(Article)

然后刷新后台管理页面，我们可以看到我们的文章管理出来了，这里你可以点进去看看，是不是发现之前添加的一些数据了，接下来我们可以丰富一下我们的数据表的字段。


## 博客数据库表设计

对于这个自用的博客设计，我们应该把重点放在博客的基础功能实现上，而一些功能的扩展如果确实有需要我们可以日后再添加。
所以对于一个基本的博客应该的数据表应该包括：用户，文章，分类三个表即可实现一个个人博客的需要的基础功能。
可能有的朋友说太少了，确实，但是以后你可以继续开发添加更多的功能。

## 设计数据库表及字段

修改上节中`models.py`的代码
修改如下：

    from django.db import models
    from django.contrib.auth.models import User#引入Django User

    class Category(models.Model):
        #分类表
        title = models.CharField(max_length=20, verbose_name = '分类名称', default = '')

    #创建文章表，通过继承models.Model来创建文章表
    class Article(models.Model):
        #文章表
        title = models.CharField(max_length=50, verbose_name = 'blog标题', default = '')#创建标题
        content = models.TextField(verbose_name = '博客正文', default = '')
        category = models.ForeignKey(Category, verbose_name = '所属分类', default = '')
        user = models.ForeignKey(User, verbose_name='文章作者', null=True, blank=True)
        #文章创建时间，这里的auto_now_add=True表示自动在数据库里创建时间。
        create_time = models.DateTimeField(verbose_name='文章创建时间', auto_now_add=True,)

这里的文章表关联分类和用户，是一对多的关联。用户表我们直接调用了`Django`自带的user表，这个稍后我们在做研究。

然后我们通过终端命令更新数据库中的表：

在blog01目录下输入：

    ➜  blog01 git:(master) ✗ python3 manage.py makemigrations
    No changes detected
    ➜  blog01 git:(master) ✗ python3 manage.py makemigrations
    No changes detected
    ➜  blog01 git:(master) ✗ python3 manage.py migrate       
    Operations to perform:
    Apply all migrations: admin, auth, contenttypes, myblog, sessions
    Running migrations:
    Applying myblog.0002_auto_20171122_0957... OK
    Applying myblog.0003_remove_article_user... OK
    Applying myblog.0004_article_user... OK
    Applying myblog.0005_auto_20171122_1032... OK
    ➜  blog01 git:(master) ✗ 


如果输入命令后报错`django.db.utils.IntegrityError: NOT NULL constraint failed: myblog_article.user_id`
请删除我们在`django shell` 中添加的测试数据，然后再修改数据表，这里其实不用删除也可以更新，需要为字段添加一个默认值`default = 1`，就可以了，当然这个我没有测试，我只是猜测。

我们启动服务器进入后台看下当前的管理页面：

![]()

我们发现并没有分类`Category`的管理连接，我们来添加上，并管理页面添加一些字段显示及搜索。
我们以分类表为例：`models.py`代码修改如下：

    class Category(models.Model):
        #分类表
        title = models.CharField(max_length=20, verbose_name = '分类名称', default = '')

        class Meta:
            verbose_name = u'博客分类'
            verbose_name_plural = verbose_name

        def __str__(self):
            return self.title

修改后，我们刷新后台管理页：

![]()

我们可以看到后台中`myblog`中的一些变化，这样后台看起来更直观了，我们继续以博客分类为例，编辑`admin.py`，修改代码：

    class CategoryAdmin(admin.ModelAdmin):
        #设置显示
        list_display = ('id',title',)

    admin.site.register(Category,CategoryAdmin)

进入后台，添加两个分类，然后效果如下图：

![]()

然后我们继续编辑`models.py admin.py`中的代码，修改文章的后台显示，具体代码请参考源文件，这里我就不贴了。
一切编辑好后我们查看一下效果：

![]()

![]()

至此，我们的后台已经有一个简单的样子啦，随着我们的博客数据库表的不断更新修改，你也应该对应的修改`admin.py`文件中的代码，这样可以在后台更方便的添加修改文章。
虽然`Django`自带的后台系统简单，但功能上基本可以满足日常需要了，做为博客的后台来用，足够了。

'''