# coding=utf-8
# 导入基本配置文件
from django import template
# 导入markdown模块
from markdown import markdown


from ..models import Article

register = template.Library()


# 自定义过滤器编写

@register.filter
def toMarkdown(str):
    ####markdown解析器
    return markdown(str)

@register.filter
def cat_count(cat_id):
    """统计分类下边的日志数"""
    return Article.objects.filter(category=cat_id).count()
