from django.contrib import admin
from .models import Article, Category


class CategoryAdmin(admin.ModelAdmin):
    #设置显示
    list_display = ('id','title',)

class ArticleAadmin(admin.ModelAdmin):
    list_display = ('id','title','content',)

admin.site.register(Category,CategoryAdmin)
admin.site.register(Article, ArticleAadmin)
