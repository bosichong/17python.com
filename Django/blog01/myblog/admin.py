from django.contrib import admin
from .models import Article, Category, UserProfile, Siteinfo



class UserProfileAdmin(admin.ModelAdmin):
    """用来显示用户相关"""
    #用来显示用户字段
    list_display = ('username','nick_name','email','gender','mobile','address')
    #过滤器设置
    list_filter = ('username','nick_name','email')
    #搜索
    search_fields = ('username','nick_name','email')


class CategoryAdmin(admin.ModelAdmin):
    #设置显示
    list_display = ('id','title',)

class ArticleAadmin(admin.ModelAdmin):
    list_display = ('title','content',)

class SiteinfoAdmin(admin.ModelAdmin):
    list_display = ('site_name','site_user','site_detail')

admin.site.register(UserProfile,UserProfileAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Article, ArticleAadmin)
admin.site.register(Siteinfo,SiteinfoAdmin)

