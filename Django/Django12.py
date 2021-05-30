#codeing=utf-8
# @Time    : 2017-12-12
# @Author  : py.sky
# @Mail    : bosichong@qq.com
# @Site    : www.17python.com
# @Title   : # 实战：利用Django开发部署自己的个人博客（12）博客分类页及搜索页的实现
# @Url     : http://www.17python.com/blog/64
# @Details : # 实战：利用Django开发部署自己的个人博客（12）博客分类页及搜索页的实现
# @Other   : OS X 10.11.6 
#            Python 3.6.1
#            VSCode 1.15.1
###################################
# 实战：利用Django开发部署自己的个人博客（12）实现博客文章的分页
###################################

'''
一不留神已经开始写滴12节了，但感觉还是有很多细节的知识点没有写到，这节说说数据分页在`Django`的实现吧。

## 数据分页

说道数据分页这个功能，在编程的日常中是经常遇到的，WEB的日常更不用说了，所以理解并熟练的掌握分页的技术可以说是很重要的了。
关于数据分页的理论这里不再做细节的讨论，我们重点来了解利用`Django`中的模块的实现方法。

## 数据分页终端下的测试

`django.core.paginator`是Django提供的一个数据分页模块，当你的分页数据量不大的时候（比如几万的数据量）可以使用这个模块。
因为这个模块需要先返回所有需要分页的数据，然后根据一定的逻辑进行分页，这就是所谓的逻辑分页吧，所以小数量分页可以直接考虑用`django.core.paginator`。
而且这个分页模块可以拿出来单独使用，就象`Django ORM`一样，可以脱离WEB环境使用，我们创建一个简单的数据来测试一下这个分布模块。

我觉得代码是最好的教程：

    ➜  ~ python3 
    Python 3.6.1 (v3.6.1:69c0db5050, Mar 21 2017, 01:21:04) 
    [GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
    Type "help", "copyright", "credits" or "license" for more information.
    >>> from django.core.paginator import Paginator
    >>> objs = [k for k in range(1000)]
    >>> p = Paginator(objs, 10)
    >>> p.count
    1000
    >>> p.num_pages
    100
    >>> p.page_range
    range(1, 101)
    >>> page1 = p.page(1)
    >>> page1
    <Page 1 of 100>
    >>> page1.object_list
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    >>> page2 = p.page(100)
    >>> page2.object_list
    [990, 991, 992, 993, 994, 995, 996, 997, 998, 999]
    >>> page2.has_next()
    False
    >>> page2.has_previous()
    True
    >>> page1.has_previous()
    False
    >>> 

通过上边的代码，我们可以看到`Paginator`对数据分页的封装是很好的，使用起来也容易理解。
接下来，我们把`django.core.paginator`引入到视图中来使用。

views.py中的代码：

    ############################
    #翻页视图中代码
    ############################
    paginator = Paginator(articles, 3)#创建Paginator
    page = request.GET.get('p')#获取当前页码
    try:
        contacts = paginator.page(page)#取得当前页码所包含的数据
    except PageNotAnInteger:
        contacts = paginator.page(1)#若不是整数，跳转到第一页。
    except EmptyPage:
        contacts = paginator.page(paginator.num_pages)#若超过了最后一页
    #############################

把上边的代码加到`return`之前即可，这里要说明一下，之前我们模板调用的数据是`articles`，现在我们需要分页提供的需要显示的数据，
这里模板中需要引用一组当前页码上需要显示的数据，这里就要使用我们传递的`contacts`，这里大家应该明白，这是当前页码需要显示的数据。
**然后把模板里的`articles`换成`contacts`，然后把模板里的`articles`换成contacts`，然后把模板里的`articles`换成`contacts`**
重要的事情要说三次。

list.html中的代码：

    <!-- 翻页  -->
    <div class="am-pagination am-pagination-centered">
        {% if contacts.has_previous %}
            <li class=""><a href="?p={{ contacts.previous_page_number }}">&laquo; 上一页</a></li>
        {% endif %}
        {% for p in contacts.paginator.page_range %}   
            <li class="{% if p == page_number %}am-active{% endif %}"><a href="?p={{ p }}">{{ p }}</a></li>
        {% endfor %}
        {% if contacts.has_next %}
            <li class=""><a href="?p={{ contacts.next_page_number }}">下一页 &raquo;</a></li>
        {% endif %}
    </div>

这里有几个变量可能是头一次看到，都是一些翻页数据变量，这组模板代码中大量的应用了`{% if XXX %}{% endif %}`标签，
还有这个翻页组件是Amaze UI提供的，笔者感觉还是不错的。
接下来就是运行服务器，预览一下效果，动手点点那些数字，看看连接是否对的上？

![]()

## 数据翻页结束了？

看了代码，大家是不是觉得太简单了？好吧这里我留个坑，有兴趣的可以自己试试，当前的数据翻页只是所有数据的翻页展示，
如果切换到某个类目下，数据太多，也需要翻页，或是搜索结果很多也需要翻页，大家想想看，根据当前提供一些代码如何扩展实现呢？

如果有问题欢迎各位可以留言给作者提问。

`django`官方 翻页帮助文档
https://docs.djangoproject.com/en/1.11/topics/pagination/





'''