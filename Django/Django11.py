#codeing=utf-8
# @Time    : 2017-12-11
# @Author  : py.sky
# @Mail    : bosichong@qq.com
# @Site    : www.17python.com
# @Title   : # 实战：利用Django开发部署自己的个人博客（11）博客分类页及搜索页的实现
# @Url     : http://www.17python.com/blog/62
# @Details : # 实战：利用Django开发部署自己的个人博客（11）博客分类页及搜索页的实现
# @Other   : OS X 10.11.6 
#            Python 3.6.1
#            VSCode 1.15.1
###################################
# 实战：利用Django开发部署自己的个人博客（11）博客分类页及搜索页的实现
###################################

'''
上节我们通过博客的模板继承及上下文沉浸器大大简化了模板的代码量，这节我们继续实现分类页及搜索结果页的展示。

## 缩短网址

之后我们访问博客地址是`http://127.0.0.1:8000/blog/home`，如果我们想直接访问地址也就是域名后直接打开博客首页怎么办？

首先修改'blog01.urls.py'中的代码：

    url(r'^', include('myblog.urls',namespace='')),#修改为直接为域名根目录，缩短网址。

去掉`r'^blog'`中的`blog`,

再修改'myblog.urls.py'中的代码：
注释掉`# url(r'^list$', v.list, name='list'),`修改为`url(r'^$', v.list, name=''),#项目首页`

运行服务器，直接访问：`http://127.0.0.1:8000`，这时直接打开的是博客列表页展示的首页。

## Django实现博客分类页展示

首页展示的是所有文章页，我想点击分类显示为分类下边的相关文章，这个如何实现？
首先我们看下点击分类后，url的格式`http://127.0.0.1:8000/?c=2`这个分类页的连接中包括一个典型的get参数，
我们可以在视图中获得这个参数2,然后再搜索所有分类`id=2`的文章，然后返回给模板即可展示出来结果了。

编写视图文件的代码

    c = request.GET.get('c', '')
    if c:
        #搜索分类ID为c的所有文章，如果分类id为空，这里就返回所有文章。
        articles = articles.filter(category=c,).order_by('-create_time')

这里的变量c，通过`request.GET.get('c', '')`获取页面上的C的`key`，`request.GET['c']`也可以访问，但不安全。
然后通过`Django`中提供数据过滤`.filter`搜索出相关的文章，然后排序后返回给模板，模板那边的代码都不用修改即可正常显示。
好了，我们访问`http://127.0.0.1:8000/?c=2` 所有分类`id=2`文章就搜索出来了。

## 搜索结果页面

在当前的页面上边有个搜索框，这是一个搜索的入口，我们希望用户通过这个搜索框进行一些模糊搜索，比如根据关键字搜索标题或正文中是否包含关键字，然后返回搜索结果展示。
说到搜索，其实首先想到的是应该对这个搜索关键字做一些限制，比如长度，还有就是安全sql注入等。
我们的搜索结果url地址`http://127.0.0.1:8000/?s=Python`，应该是这个相似。
这里我们采用django提供的一个表单框架来实现当前的搜索功能，接下来开始编写代码。

创建myblog.forms.py:

    #coding=utf-8
    from django import forms

    class Searchform(forms.Form):
        #搜索表单定义
        s = forms.CharField(max_length=20)

就这点代码，定义了一个表单。

在视图`myblog.views.py`中使用,先引用

    from .forms import Searchform

然后编写代码

    s = ''#搜索关键字
    #以下判断表单是否验证成功，如果验证成功返回一个字符串s
    if request.method == 'GET':
        form = Searchform(request.GET)
        if form.is_valid():
            s = request.GET.get('s')
    if s :
        articles = articles.filter(Q(title__contains=s)|Q(content__contains=s)).order_by('-create_time')

这里有个Q函数记得引用一下`from django.db.models import Q#模糊查询多个字段使用`,这个Q函数是关键字查询中经常使用到的，详细了解请百度。

然后模板里修改一下模板`base.html`中搜索框的代码：

    <form class="am-topbar-form am-topbar-left am-form-inline am-topbar-right"  action="{% url '' %}">
      <div class="am-form-group">
        <input type="text" class="am-form-field am-input-sm" placeholder="搜索文章" name="s">
      </div>
      <button type="submit" class="am-btn am-btn-default am-btn-sm">搜索</button>
    </form>

`{% url '' %}`这是模板中的标签，Django中提供了很多模板标签，如果需要详细了解可以查看官方的文档。

好了，我们刷新首页，然后在搜索框里输入:10 就会搜索标题有含有10的文章了，


![]()

到此我们的分类页及搜索结果页面的功能就实现了。
如果在修改中发现了错误，可以复制留言中的错误回复，站长看到会帮助解答的。另外可以查看源文件核对，看看自己哪里改的不对，也能发现错误。



'''