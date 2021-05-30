#codeing=utf-8
# @Time    : 2017-12-02
# @Author  : J.sky
# @Mail    : bosichong@qq.com
# @Site    : www.17python.com
# @Title   : # 实战：利用Django开发部署自己的个人博客（7）扩展User表及完善blog数据库表。
# @Url     : http://www.17python.com/blog/59
# @Details : # 实战：利用Django开发部署自己的个人博客（7）扩展User表及完善blog数据库表。
# @Other   : OS X 10.11.6 
#            Python 3.6.1
#            VSCode 1.15.1
###################################
# 实战：利用Django开发部署自己的个人博客（7）扩展User表及完善blog数据库表。
###################################

'''

到目前为止，我们基本上初步的了解了Django使用，我们搭建了一个简单的blog雏形，接下来我们将在这个基础之上进行blog数据模型的完善，使之更接近我们自己的需求。

## 扩展用户user表

Django自带了一个user表，可以满足一些简单的用户资料数据，我们看下表的结构：

!()[]

这个表结构很简约，有些我们需要的并没有，所以我们只有通过扩展它来进行添加字段，官方及网上介绍了几种扩展user表的方法，这里我只介绍一种本人认为比较实际的。

首先在model.py中引入django的AbstractUser：

    from django.contrib.auth.models import AbstractUser

然后编写代码扩展user:

    class UserProfile(AbstractUser):
        """继承django系统自带的user创建用户表，
        1.配置文件中要添加 AUTH_USER_MODEL = "blog.UserProfile"
        2.引入from django.contrib.auth.models import AbstractUser
        3.admin.py 中注册用户表 admin.site.register(UserProfile)
        4. 如果之前先生成了数据库表，之后修改的user要重新生成表，最好先清空数据库。
        """
        nick_name = models.CharField(max_length=24, verbose_name='用户昵称', default='')
        gender = models.CharField(max_length=10, choices=(('1','男'),('0','女')), default='1', verbose_name='用户性别')
        birday = models.DateField(verbose_name='用户生日',null=True, blank = True)
        mobile = models.CharField(max_length=11, null=True, blank=True,verbose_name='电话号码')
        address = models.CharField(max_length=200, verbose_name="用户地址", default='')
        detail = models.CharField(max_length=200, verbose_name="个人简介", default='')

        class Meta(AbstractUser.Meta):
            verbose_name=u'用户表'
            verbose_name_plural = verbose_name
        def __unicode__(self):
            return self.username

修改Article中的一处用户引用：

    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='文章作者', null=True, blank=True)

这里为了能调用settings.AUTH_USER_MODEL变量，我们必须在文件中引用配置文件`from blog01 import settings`

修改admin.py中的代码：

    class UserProfileAdmin(admin.ModelAdmin):
        """用来显示用户相关"""
        #用来显示用户字段
        list_display = ('username','nick_name','email','gender','mobile','address')
        #过滤器设置
        list_filter = ('username','nick_name','email')
        #搜索
        search_fields = ('username','nick_name','email')

    admin.site.register(UserProfile,UserProfileAdmin)

经过以上配置，我们的用户表扩展基本上准备好了，然后我们终端下运行命令修改生成数据库：

    python3 manage.py makemigrations
    python3 manage.py migrate

这个时候会报错，这里的报错，笔者也是研究了一阵子，一直没有找到很好的解决方法，目前解决的方法只有一种：
删除当前的数据库，重新生成一个新的数据库，这种方法显然不是很好，但目前只能这样解决。
所以对于学习的项目来说问题不大，如果你准备生新设计一个blog的时候，记得一定要先扩展用户表，这样的话就不需要重新生成所有表了。
切记：先扩展用户表 先扩展用户表 先扩展用户表 ！

由于用数据库是生新生成的，所以我们的管理员也就不存在了，就当复习一下，我们重新创建一个管理员：

    python3 manage.py createsuperuser

设置相关的选项，运行服务器：`python3 manage.py runserver `,
http://127.0.0.1:8000/admin/
管理员又可以在后台登陆了，我们登陆一下看看后台有什么变化？

!()[]
!()[]

可以看到，我们多了一个用户表，编辑用户，可以看到多了一些用户的选项，到此为止我们的用户表扩展完毕。
总结扩展：继承django系统自带的user创建用户表，
1.配置文件中要添加 AUTH_USER_MODEL = "blog.UserProfile"
2.引入from django.contrib.auth.models import AbstractUser
3.admin.py 中注册用户表 admin.site.register(UserProfile)
4.如果之前先生成了数据库，之后需要扩展user表则要重新生成数据库。
其中第4步，笔者并不满意，但目前没有找到解决的方法，希望有大侠提供一下不用删除重建数据库的方法。

## 完善其它数据表

目前我们的数据表中有UserProfile,Category,Article。这个实现性的blog我打算再加入一个表Siteinfo，用来记录站点中的一些相关信息，
还会再添加一个SiteImages相册的表，后继我们再继续研究上传图片的相关设置。

关于的表的扩展也没什么好说的我直接贴表的代码，通过verbose_name就能看明白这个字段的含意了。


    class Category(models.Model):
        title = models.CharField(max_length=20, verbose_name = '分类名称', default = '')
        daitail = models.CharField(max_length=100, verbose_name='分类介绍', default='')
        icon = models.CharField(max_length=100, verbose_name='分类图标', default='')
        sort_id = models.IntegerField(verbose_name='分类排序', default=99)

        class Meta:
            verbose_name = u'博客分类'
            verbose_name_plural = verbose_name

        def __str__(self):
            return self.title

    class Article(models.Model):
        title = models.CharField(max_length=50, verbose_name = '文章标题', default = '')#创建标题
        article_synopsis = models.TextField(verbose_name=u'日志简介', default='')
        content = models.TextField(verbose_name = '博客正文', default = '')
        category = models.ForeignKey(Category, verbose_name = '所属分类', default = '')
        user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='文章作者', null=True, blank=True)
        #文章创建时间，这里的auto_now_add=True表示自动在数据库里创建时间。
        create_time = models.DateTimeField(verbose_name='文章创建时间', auto_now_add=True,)
        update_time= models.DateTimeField(verbose_name=u'更新时间',  auto_now=True)

        class Meta:
            verbose_name = u'博客文章'
            verbose_name_plural = verbose_name

        def __str__(self):
            return self.title

    class Siteinfo(models.Model):
        site_name = models.CharField(max_length=20, verbose_name=u'站点名称', default='')
        site_detail = models.CharField(max_length=100, verbose_name=u'站点介绍', default='')
        site_user = models.ForeignKey(UserProfile, verbose_name='管理员', null=True, blank=True)
        site_footer = models.TextField(verbose_name='站点底部代码', default='')

        class Meta:
            verbose_name = u'网站信息'
            verbose_name_plural = verbose_name

        def __str__(self):
            return self.site_name

每个人对于自己的博客功能需求都不一样的，所以你可以根据自己的需要进行删减，修改完代码后终端运行全集进行更新：

    python3 manage.py makemigrations
    python3 manage.py migrate

上边的命令是不是已经很熟悉了？你会发现Django更新数据表真是很方便。
更新后，如果终端没有错误提示就表示数据表更新完成了，为了在admin后台显示信息更完整，我们还需要更新一下admin.py这个文件，
设置自己需要显示的内容，这里我就不贴代码了，具体参考git上的源文件好了。

然后启动服务器，我们看下后台数据是不是显示出来了，也可以在数据库管理软件中查看一下数据表结构。

!()[]
!()[]

后台中我们看到了网站信息，这里记录了站点名称及一些站点内容，当然字段你可以继续丰富起来，好了，我们添加一个站点信息，方便以后调用。

!()[]

站点底部代码这个文本字段其实就是以后用来放置一些需要经常修改的代码，有时候我们调用第三方代码比如统计、搜索蜘蛛等代码时候需要经常修改，
这时只需要在网站后台修改这些代码即可，就没有必要去修改源文件了。保存后，你的站点id就是1因为只有一个网站。

然后再添加一些博客文章备用，尽量多添加些，最好10篇以上，稍后我们会做翻页处理。




'''