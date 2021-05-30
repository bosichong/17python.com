#codeing=utf-8
# @Time    : 2017-12-07
# @Author  : J.sky
# @Mail    : bosichong@qq.com
# @Site    : www.17python.com
# @Title   : # 实战：利用Django开发部署自己的个人博客（8）构建Blog首页
# @Url     : http://www.17python.com/blog/60
# @Details : # 实战：利用Django开发部署自己的个人博客（8）构建Blog首页
# @Other   : OS X 10.11.6 
#            Python 3.6.1
#            VSCode 1.15.1
###################################
# 实战：利用Django开发部署自己的个人博客（8）构建Blog首页
###################################

'''
07节我们基本上完成了Blog数据模型的后端构建，06节我们结合模板简单渲染了一个博客文章页，这样的话，你只需要在blog的模板中添加一些标签就可以扩展详情页的展示内容了。

## Blog首页的构建

Blog首页我们这里定义一些展示内容：导航，搜索框，博客最新文章（10篇左右），博客分类及标签展示，站长简介等。这并不是完整的构建清单，你也可以根据自己的需要添加更多的更酷的功能。

## Blog导航

关于站点的导航，我这里有两种建议：

1. 直接在html中手动添加修改，可能有的同学说不方便，其实导航这东西固定后基本上很少修改，如果html熟练可以考虑这个方法。
2. 在数据库添加一个导航表，表字段包括：`id,name,url` 再添加一个排序的字段，这样你可以调用数据库读取数据后在模板中渲染出来，这种适合经常修改导航的同学。

## 博客首页最新文章

blog首页最新文章，这个和文章详情页有些相似，只不过首页渲染的是多篇文章页只是渲染一篇文章而已。
好吧，我们回忆一下`Django`实现步骤，先建立数据模型（已经搞定），再编写视图代码及设置路由，最后在模板里渲染。
其实，一个简单的Blog只需要二个视图方法：bloglist,blog 分别代表blog列表和文章详情页。
models中的代码之前编写过了，如果功能有扩展需要可以自己修改models。

list视图代码编写:

    def bloglist(request):
        #blog列表页
        #返回所有日志列表，以创建时间排序。
        articles = Article.objects.all().order_by('-create_time')

        #把调用的数据传递给模板
        return render(request, 'list.html', {'articles':articles,})

我们先创建一个`list.html`模板,把`blog.html`中的代码复制过去，我在此基础上修改即可。
运行服务器后，我们访问`http://127.0.0.1:8000/blog/blog/1`
我们看blog页面上只显示了一篇文章，如果我们循环输出视图传过来的博客数据即可打印所有文章在当前页面。
`list.html`中我们只小小的修改一下代码，添加一个循环进去即可。

`list.html`代码：

    {% for article in articles %}
        <article class="blog-main">
            <h3 class="am-article-title">
            <a href="#">{{ article.title }}</a>
            </h3>
            <h4 class="am-article-meta blog-meta">发布时间：2014/06/17</h4>
    
            <div class="am-g blog-content">
            {{ article.content }}
            </div>
        </article>
    
        <hr class="am-article-divider blog-hr">
        {% endfor %}

`urls.py`中添加一个路由：

    url(r'^list$', v.list, name='list'),

最后测试之前，如果你还没有添加数据，建议添加10篇博客文章及博客类目
然后我们访问：`http://127.0.0.1:8000/blog/list`

![]()

看，博客首页的文章渲染出来了，但是我还想显示文章作者和所属于类目怎么办？
我们只需要编辑修改`<article>`中的代码即可，修改如下：

     {% for article in articles %}
        <article class="blog-main">
            <h3 class="am-article-title">
            <a href="#">{{ article.title }}</a>
            </h3>
            <h4 class="am-article-meta blog-meta">发布时间：2014/06/17</h4>
            <p>作者：{{ article.user.nick_name }} 分类：{{ article.category }}</p>
            <div class="am-g blog-content">
            {{ article.article_synopsis }}
            </div>
        </article>
    
        <hr class="am-article-divider blog-hr">
    {% endfor %}

`{{ article.user.nick_name }}`是通过一对多关联进行搜索，返回user，然后再显示昵称。

刷新页面查看，我们看到作者及分类都显示出来了，而且我们把详细内容更换成了日志简介显示。

![]()

至此首页上的文章列表显示出来了，你也可以通过此方法继续更新详情页上的内容展示，还可以更新右侧的分类展示及个人简介。
分类及个人简介的代码这里我就不贴了，如果自己实在写不出，就下载源码看看。


'''