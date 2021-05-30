from django.contrib import admin
from .models import Article, Category, UserProfile, Siteinfo, Blogimage

from django.utils.safestring import mark_safe



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

admin.site.register(UserProfile,UserProfileAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Article, ArticleAadmin)
admin.site.register(Siteinfo,SiteinfoAdmin)

