from django.db import models
#创建文章表，通过继承models.Model来创建文章表
class Article(models.Model):
    title = models.CharField(max_length=50, verbose_name = 'blog标题', default = '')#创建标题
    content = models.TextField(verbose_name = '博客正文', default = '')
