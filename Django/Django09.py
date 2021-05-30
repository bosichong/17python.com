#codeing=utf-8
# @Time    : 2017-12-08
# @Author  : py.sky
# @Mail    : bosichong@qq.com
# @Site    : www.17python.com
# @Title   : # 实战：利用Django开发部署自己的个人博客（9）Django模板的继承
# @Url     : http://www.17python.com/blog/61
# @Details : # 实战：利用Django开发部署自己的个人博客（9）Django模板的继承
# @Other   : OS X 10.11.6 
#            Python 3.6.1
#            VSCode 1.15.1
###################################
# 实战：利用Django开发部署自己的个人博客（9）Django模板的继承
###################################
'''
从上一节开始，我们将一直持续和前端的渲染打交道了，当前我们的blog有两个前端的模板页，后继会因为功能的扩展出现更多的模板页，
我们发现模板页中大部分代码都是相同的，我们只修改其中的一部分代码，那么我们能不能通过某些方法来重用这些代码，这样方便以后的代码修改。
答案是有的，`Django`提供了一个模板继承的功能，它可以让你引用或包含一些模板上共用的代码。

## `Django`模板中的代码引用

blog的页面中有很多重复的代码，比如导航，站点底部，一些广告代码，侧边的分类标签等信息，这些需要重复使用的代码我们不要到处复制，
这样以后如果修改的话就会有很多麻烦，我们应该建立相应的模板页，然后通过继承来使用，这样会大大减少我们的代码编写工作量。

我们创建`myblog.templates.base.html`复制`list.html`中所有的代码粘贴过去。
关于模板中定义使用的代码主要有1种：

    {% block site_title %}blog{% endblock site_title %}

`block`定义，引用后可以在继承页上修改`site_title`的标题。

    {% block article %} 文章列表内容 {% endblock article %}

比如上边我又定义了一下文章列表内容的引用模块`block`，我们看下`list.html`中是如何引用这些`block`

`list.html`的代码基本上可以变的很简单了，首先最上边要加入引用需要继承的父类模板页，然后添加需要修改的引用代码：

    {% extends 'base.html' %}
    {% block site_title %}MyDjangoBlog~~~~~{% endblock site_title %}
    {% block article %} 
    {% for article in articles %}
    <article class="blog-main">
        <h3 class="am-article-title">
        <a href="#">{{ article.title }}</a>
        </h3>
        <h4 class="am-article-meta blog-meta">发布时间：2014/06/17</h4>
        <p>作者：{{ article.user.nick_name }} 分类：{{ article.category }}</p>
        <div class="am-g blog-content">
        {{ article.content }}
        </div>
    </article>
    <hr class="am-article-divider blog-hr">
    {% endfor %}
    {% endblock article %}

不会吧？`list.html`就变成这么点代码了？我们运行一下服务器,然后访问`http://127.0.0.1:8000/blog/list`
和之前一样没毛病！真是强大的模板继承功能，其实我非常喜欢这个功能！

照猫画虎，把`blog.html`也修改了！

    {% extends 'base.html' %}
    {% block site_title %}{{ article.title }}{% endblock site_title %}
    {% block article %} 
    <article class="blog-main">
        <h3 class="am-article-title">
        <a href="#">{{ article.title }}</a>
        </h3>
        <h4 class="am-article-meta blog-meta">发布时间：2014/06/17</h4>
        <p>作者：{{ article.user.nick_name }} 分类：{{ article.category }}</p>
        <div class="am-g blog-content">
        {{ article.content }}
        </div>
    </article>
    {% endblock article %}

我们访问`http://127.0.0.1:8000/blog/blog/1` 结果也是很明显的，让我们继续感叹一下`block`继承功能的强大吧



'''