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