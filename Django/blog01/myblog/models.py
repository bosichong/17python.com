from django.db import models
from django.contrib.auth.models import User#引入Django User


class Category(models.Model):
    #分类表
    title = models.CharField(max_length=20, verbose_name = '分类名称', default = '')

    class Meta:
        verbose_name = u'博客分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title

#创建文章表，通过继承models.Model来创建文章表
class Article(models.Model):
    #文章表
    title = models.CharField(max_length=50, verbose_name = '文章标题', default = '')#创建标题
    content = models.TextField(verbose_name = '博客正文', default = '')
    category = models.ForeignKey(Category, verbose_name = '所属分类', default = '')
    user = models.ForeignKey(User, verbose_name='文章作者', null=True, blank=True)
    #文章创建时间，这里的auto_now_add=True表示自动在数据库里创建时间。
    create_time = models.DateTimeField(verbose_name='文章创建时间', auto_now_add=True,)

    class Meta:
        verbose_name = u'博客文章'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title



    
    
