#codeing=utf-8
# @Time    : 2017-12-14
# @Author  : py.sky
# @Mail    : bosichong@qq.com
# @Site    : www.17python.com
# @Title   : # 实战：利用Django开发部署自己的个人博客（13）Markdown模块解析Markdown代码
# @Url     : http://www.17python.com/blog/65
# @Details : # 实战：利用Django开发部署自己的个人博客（13）Markdown模块解析Markdown代码
# @Other   : OS X 10.11.6 
#            Python 3.6.1
#            VSCode 1.15.1
###################################
# 实战：利用Django开发部署自己的个人博客（13）Markdown模块解析Markdown代码
###################################

'''
使用`Django`编写个人博客是一件很轻松的事，`Django`给我们提供了很多功能模块，让我们大大减少了代码的编写，让我们把更多的精力集中到程序的逻辑开发上，让我们有更多的时间去陪家人、陪孩子和打游戏。
发自心的感谢:感谢`Django`，感谢开源界的程序员及一切。

## 引入`Markdown`

博客有了，不过文章内容页上只显示的是字符，并没有任何美化的效果，比如插入图片、加入一些样式等，解决这个问题做为一个程序员首先就会想到`Markdown`，
`python3`中有`Markdown`模块，我们先来安装一下：

    pip3 install markdown

## 使用`Markdown`

    ➜  ~ python3
    Python 3.6.1 (v3.6.1:69c0db5050, Mar 21 2017, 01:21:04) 
    [GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
    Type "help", "copyright", "credits" or "license" for more information.
    >>> from markdown import markdown
    >>> s = '###这里是标题'
    >>> m = markdown(s)
    >>> m
    '<h3>这里是标题</h3>'

额，又是这么简单，接下来就是引入到`Django`中使用了。
插播一条广告：如果你对`Markdown`语法不了解，请看下边的博文。
[Markdown 语法学习总结](http://www.17python.com/blog/5)

## `Django`模板中输出`html`

启动服务器，我们添加一篇带有`markdown`语法的文章:

    #Markdown文章测试哦
    ##Markdown文章测试哦Markdown文章测试哦

    1. Markdown文章测试哦
    2. Markdown文章测试哦
    3. Markdown文章测试哦


    <h1>html测试哦</h1>
    <br/>
    <h3>html测试哦html测试哦html测试哦</h3>

打开这个篇博文的页面，我们会看到如下效果：

![]()

发现`Markdown`语法只是原样输出，并没有解析，还有就是`html`代码被转义了，没有在网页中显示出样式，好了，发现两个问题，我们逐一解决。

## 关闭`Django`模板中的`html`转义

关闭`Django`模板中的`html`转义有两种方法：


    <p>这行不会被转义</p>: {{ data }}
    <p>这行会被自动转义</p>: {{ data|safe }}

这种是比较短小的`html`情况下使用的过滤器`safe`来关闭`html`转义，如果是大段的`html`代码比如博文，我们使用下边的方法：


       {% autoescape off %}
        {{ article.content }}
       {% endautoescape %}

其中`article.content`输出的`html`代码就不会被转义了，网页上就会显示出具体的样式。我们试下。

打开`bolg.html`,修改模板内容渲染：

    {% autoescape off %}
        {{ article.content }}
    {% endautoescape %}

保存后，我们刷新一下页面看看，

![]()

`html`代码已经被正常输出了，网页上显示了还的标题样式，但我们发现`markdown`的语法还没有被解析成`html`代码。

## 使用`Django`自定义过滤器+`Markdown`模块解析`Markdown`代码

创建自定义过滤器文件`myblog.templatetags.mytags.py`,并在相同目录中添加`__init__.py`空文件即可。

先编写`mytags.py`过滤器代码：

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

然后我们在模板中引用一下这个过滤器，

编辑修改`blog.html`的代码，在头部添加：

    {% load mytags %}

表示加载自定义的过滤器，修改渲染文章内容处的代码，添加过滤器，过滤器的用法很简单，具体看代码：

    {% autoescape off %}
        {{ article.content|toMarkdown }}
    {% endautoescape %}

保存后，我们刷新文章页查看一下:

![]()

到此，`markdown`已经在我们的博客中完美引用了，当然做为一个程序员我们经常和代码打交道，博客中少不了要贴代码，所以代码美化也是少不了的。
这里我推荐一个代码美化的js：`highlight.js`去他的官方网站上下载一个喜欢的js和css样式，然后加到`blog.html`中，大体上如下：

    <link rel="stylesheet" href="/static/highlight/styles/atom-one-light.css">
    <script src="/static/highlight/highlight.pack.js"></script>
    <script>hljs.initHighlightingOnLoad();</script>

具体文件请按目录保存，这样你的博客中的代码就有了自己的样式，而不是很单一的颜色了。

好了，这节结束，感觉很简单的东西，怎么写了么这长。。。。。。有问题请在下边留言给俺

'''