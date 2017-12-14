#coding=utf-8
#导入基本配置文件
from django import template
#导入markdown模块
from markdown import markdown
#引入过滤器
register = template.Library()

#自定义过滤器编写

@register.filter
def toMarkdown(str):
    ####markdown解析器
    return markdown(str)

