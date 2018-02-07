#coding=utf-8
from django.conf import settings as original_settings#必须引入
from myblog.models import UserProfile, Category, Siteinfo, Article#导入一些必须的model

from random import shuffle

def blog_info(request):
    #站长及博客上下文数据管理
    userinfo = UserProfile.objects.get(pk=1)#站长资料
    siteinfo = Siteinfo.objects.get(pk=1)#blog相关资料
    categorts = Category.objects.all().order_by('sort_id')#根据排序获取所有分类


    l = Article.objects.values("tag")#获得所有文章的标签
    tags = []#所有标签数据
    #清洗数据，把重复的去除
    for k in l :
        tlist = k["tag"].split(' ')
        for item in tlist:
            if item not in tags:
                tags.append(item)#加入list

    shuffle(tags)#重新洗牌，随机显示
    print(tags)
    #定义TAGcss的样式，用来随机显示背景颜色
    tagcss =['am-radius','am-badge-primary','am-badge-secondary','am-badge-success','am-badge-warning','am-badge-danger']
    #把获取的数据通过字典返回
    return {'userinfo':userinfo, 'siteinfo':siteinfo, 'categorts':categorts, 'tags':tags, 'tagcss':tagcss}





