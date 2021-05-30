#codeing=utf-8
# @Time    : 2017-12-14
# @Author  : py.sky
# @Mail    : bosichong@qq.com
# @Site    : www.17python.com
# @Title   : # 实战：利用Django开发部署自己的个人博客（14）Django实现图片的上传和引用
# @Url     : http://www.17python.com/blog/66
# @Details : # 实战：利用Django开发部署自己的个人博客（14）Django实现图片的上传和引用
# @Other   : OS X 10.11.6 
#            Python 3.6.1
#            VSCode 1.15.1
###################################
# 实战：利用Django开发部署自己的个人博客（14）Django实现图片的上传和引用
###################################
'''
我们利用`Django`搭建的博客虽然很简陋，但功能也算很全了（这里应该有一个偷笑的表情），很全吗？还不能在博客中上传及加入图片，
这确实是一个很重要的功能，一个博客很多地方需要用到上传图片这个功能，比如博文中插入图片，头像，站点美化等，这节我们就用`Django`实现一下图片上传。

## Django搭建简易相册

如果博客中需要插入图片，当然还是存放在自己的域名下比较好，一来容易备份，也减少了网站中的外部链接，本次只是为博客搭建一个极其简单的小相册，
如果各位大侠对功能上有更高级的需求，建议查阅相关资料扩展一下哈。

## 安装Pillow

图片上传需要先安装Pillow模块支持 `pip install Pillow`

## 相册models编写

我们先来编写相册的数据模型，修改`myblog.models.py`,添加如下代码：

    class Blogimage(models.Model):
        #博客相册
        title = models.CharField(max_length=20, verbose_name='图片标题', default='')
        path = models.ImageField(verbose_name='图片', upload_to='upload/%Y/%m', default='upload/default.jpg', max_length=100)
        
        class Meta:
            verbose_name = '网站相册'
            verbose_name_plural = verbose_name

        def __ser__(self):
            return self.title

接下来修改配置`myblog.admin.py`中的代码,这里的设置是用来在`admin`后台显示图片：

    class BlogimageAdmin(admin.ModelAdmin):
        list_display = ('title', 'image_url', 'image_data')
        readonly_fields = ('image_url', 'image_data') #这里必须加上这行，表明为自定义的字段属性
        # 通过两个函数返回自定义字段的数据
        def image_url(self, obj):
            #from django.utils.safestring import mark_safe
            #mark_safe 是用来取消html转义。
            return mark_safe('<a href="%s">右键复制图片地址</a>' % obj.path.url)
        def image_data(self, obj):
            return mark_safe('<img src="%s" width="100px" />' % obj.path.url)

        # 页面显示的字段名称
        image_data.short_description = u'图片'
        image_url.short_description = u'图片地址'

    admin.site.register(Blogimage,BlogimageAdmin)

然后再修改配置文件`settings.py`,添加如下代码进行上传文件目录设置：

    #设置上传文件目录
    MEDIA_URL = '/media/'
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

最后再设置一个路由blog01.urls.py

    #配置上传文件的访问处理函数
    # 引入from django.views.static import serve
    url(r'^media/(?P<path>.*)$',  serve, {"document_root":MEDIA_ROOT}, name='media'),

好了，我们在运行服务器前，在终端先更新创建数据表:

    ➜  blog01 git:(master) ✗ python3 manage.py makemigrations
    Migrations for 'myblog':
    myblog/migrations/0003_blogimage.py
        - Create model Blogimage
    ➜  blog01 git:(master) ✗ python3 manage.py migrate
    Operations to perform:
    Apply all migrations: admin, auth, contenttypes, myblog, sessions
    Running migrations:
    Applying myblog.0003_blogimage... OK


创建表后，运行服务器，登陆后台看下，发现有了网站相册这个后台管理，我们上传一张图片，然后编辑图片查看效果：

![]()

一个简单的相册就搭建成功了，右键复制图片地址，试一下是不是可以打开图片并预览，这样的话我就可以把图片插图到博文里了，
当然你也可以继续扩展user表，添加头像功能，也可以扩展站点信息加入logo 个性图标等，就看你是如何设计的了。
虽然我提供的方法很简单，但功能足够了，如果你想拥有更强大的后台，那就需要你自己去编写了，加油少年，我看好你！


'''