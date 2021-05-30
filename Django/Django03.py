#codeing=utf-8
# @Time    : 2017-11-10
# @Author  : J.sky
# @Mail    : bosichong@qq.com
# @Site    : www.17python.com
# @Title   : 实战：利用Django开发部署自己的个人博客（3）Template: Django模板
# @Url     : http://www.17python.com/blog/54
# @Details : 实战：利用Django开发部署自己的个人博客（3）Template: Django模板
# @Other   : OS X 10.11.6 
#            Python 3.6.1
#            VSCode 1.15.1
###################################
# 实战：利用Django开发部署自己的个人博客（3）Template: Django模板
###################################

'''
一般WEB框架构建几乎相同，都会有路由，视图，模板，中间件等大多功能相同的组件，`Django`也有自己的`Template: Django模板`。

## 配置及使用`Django`的模板

依然使用第一节创建的是项目，创建`myblog.templates.home.html`。

    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Home Page</title>
    </head>
    <body>
        {{ s }}
    </body>
    </html>

然后编写视图文件`myblog.views.py`代码：

    def home(request):
        s = 'Hello World!'
        return render(request,'home.html',{'s':s})

配置路由`mybolg.urls.py`添加代码：

    url(r'^home$', v.home, name='home'),

到此一组路由、视图、模板就配置完了，启动服务器：`python3 manage.py runserver`
打开网址：`http://127.0.0.1:8000/blog/home` 你会看到如下图：
![]()

## 继续深入模板

我们修改视图`myblog.views.py`中的代码如下：

    def home(request):
        s = 'Hello World!'
        l = [1,2,3,4,5,6,7,8]
        info_dict = {'h': 'hello', 'w': 'world'}
        return render(request, 'blog/home.html', {'s':s, 'l':l, 'info_dict':info_dict})

这次我们添加了一个列表，一组字典，看看在模板中是如何渲染这类数据的。

继续修改`myblog.templates.home.html`:

    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Home Page</title>
    </head>
    <body>
        {% comment %} 变量输出 {% endcomment %}
        <h1>{{ s }}</h1>
        <br/> {% comment %} 循环输出list {% endcomment %} {% for i in l %} {{ i }} {% endfor %}
        <br/> {% comment %} 字典输出 {% endcomment %} {{ info_dict.h }} {{ info_dict.w }}
        <br/> {% comment %} 循环输出字典 {% endcomment %} {% for key, value in info_dict.items %} {{ key }} : {{ value }} 
        {% endfor %}
    <h1><a href="{% url 'blog:home' %}">测试</a></h1>
    </body>
    </html>

刷新查看一下网页
![]()

是不是感觉`Django`模板中的沉浸很方便？我们几行代码就渲染了列表，字典。

## 一些常用标签

    # 变量
    ## 通过下标获取列表变量的值
    {{ names.0 }}

    # 注释
    {# 单行注释 #}
    {% comment %}多行注释{% endcomment %}

    # url路由
    有这样一个路由
    url(r'^blog/', 'myapp.views.blog'), # 博客页面
    那么就这样使用
    {% url 'digital.views.blog' %}
    或者使用别名，例如
    url(r'^blog/', 'myapp.views.blog', name='blog'),
    {% url 'blog' %}
    如果是其他app的url，那么需要带上该app的namespace，首先在定义的时候需要添加namespace，如
    url(r'^oauth/', include('oauth.urls', namespace='oauth'))
    然后在实用url的时候：
    {% url 'oauth:hello' %}

    # for循环
    {% for <element> in <list> %}{% endfor %}
    {% for <element> in <list> reversed%}{% endfor %} 反向迭代列表
    {% for <element> in <list> %}{% empty %}{% endfor %} 列表为空时的输出内容
    {{ forloop.counter }}   # 获取当前索引，默认从1开始
    {{ forloop.counter0 }}  # 获取当前索引，从0开始

    # if语句
    {% if <element> %}
    {% elif <element> %} 
    {% else %}
    {% endif %}

    {% ifequal 变量1 变量2 %}
    比较值
    {% endifequal %}
    ifnotequal同上
    # autoescape标签

    {% autoescape on %}       # 去掉自动转义
    {{ body }}
    {% endautoescape %}

    # cycle标签：每次使用该标签，标签中的值就会变化，比如下面这个，第一次该值为row1，第二次则为row2，第三次又变为了1，感觉可以用于循环里面的奇偶什么的
    {% for o in some_list %}
    <tr class="{% cycle 'row1' 'row'2 %}
    ...
    </tr>
    {% endfor %}

    # now 标签，直接将当前时间按指定格式输出：
    {% now "jS F Y H:i" %}

    # spaceless标签：移出HTML tags之间的空白
    {% spaceless %}
    <p>
    ...
    </p>
    {% endspaceless %}

    # verbatim：停止模版引擎，一般用于在模板里面写Javascript什么的
    {% verbatim %}
    ...
    {% endverbatim %}

    # with标签：和语法里面的with类似
    {% with total=business.employees.count %}
    {{ total }} employee{{ total|pluralize }}
    {% endwith %}

关于模板强大的功能还有很多，建议参考官方文档进行查阅。

本文部分代码引自 [我的Django手册](http://www.jianshu.com/p/bc6d8f03eacf?utm_source=desktop&utm_medium=timeline)



'''