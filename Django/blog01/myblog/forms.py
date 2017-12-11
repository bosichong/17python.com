#coding=utf-8
from django import forms

class Searchform(forms.Form):
    #搜索表单定义
    s = forms.CharField(max_length=20)