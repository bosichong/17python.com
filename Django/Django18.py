#codeing=utf-8
# @Time    : 2018-03-16
# @Author  : py.sky
# @Mail    : bosichong@qq.com
# @Site    : www.17python.com
# @Title   : 实战：利用Django开发部署自己的个人博客（18）博客的Robots与sitemap.xmlitemaps
# @Url     : http://www.17python.com/blog/81
# @Details : 实战：利用Django开发部署自己的个人博客（18）博客的Robots与sitemap.xml
# @Other   : OS X 10.11.6
#            Python 3.6.1
#            PyCharm
###################################
# 实战：利用Django开发部署自己的个人博客（18）博客的Robots与sitemap.xml
###################################

'''
好久没有更新blog了，想了很多理由来解释，看转念一想也没有多少人看这些无聊的东西，所以解释也是多余的哈：）
网站的`Robots`与`sitemap.xml`大家都知道不？这二个都是与搜索引擎有关的，如果你很重视SEO，那么你的blog应该有这二个文件。


## Robots的实现

`Robots.txt`就是一个文本，如果你对搜索引擎收录没有拒绝，那个这个文件的能容很简单的：
1.设置一条路由：


    url(r'^robots\.txt$', v.robots), #robots


2.在视图中添加一个方法对应路由：

    # robots
    def robots(request):
        return HttpResponse('User-agent: *')

我们的目的很简单，就是要输出一行简短的字符串：`User-agent: *`，用来告诉搜索引擎：来吧，请收录我，我是没有任何拒绝的！

运行服务器，在地址栏中输入
`http://127.0.0.1:8000/robots.txt`
打开后即可看到显示内容为：`User-agent: *`
好了，`blog的Robots`实现完成。

## sitemap.xml的实现

`sitemap.xml`主要用来告诉搜索引擎我的网站有哪些网页，列了一个xml清单，你可以收录了。
本代码生成的`sitemap.xml`是根据百度的站长帮助提供的资料生成的，同时也符合搜索引擎的sitemap.xml规则。

先看一下`sitemap.xml`文件需要哪些内容：


    <url>
    <loc>http://www.17python.com/blog/80</loc>
    <lastmod>2018-02-07</lastmod>
    <changefreq>daily</changefreq>
    <priority>0.8</priority>
    </url>

上边是`sitemap.xml`中的一条，我们只要关注其中的url与博文创建的时间即可，其余的只要和代码中的一样就行，当然，如果你非得要了解，可以看看百度站长站的帮助。


1. 创建URL路由，不解释：

    # sitemaps url设置
    url(r'^sitemap\.xml$', v.sitemap),

2.视图文件中的实现方法：

    # sitemap 文件生成
    def sitemap(request):
        articles = Article.objects.filter(article_type='2').order_by('-article_create_time')
        return render(request, 'sitemap.html', {'articles':articles}, content_type="text/xml")

3.创建一个模板文件内容如下：

    <?xml version="1.0" encoding="utf-8"?>
    <urlset>
        {% for ac in articles %}
        <url>
            <loc>http://www.17python.com/blog/{{ ac.id }}</loc>
            <lastmod>{{ ac.update_time | date:"Y-m-d" }}</lastmod>
            <changefreq>daily</changefreq>
            <priority>0.8</priority>
        </url>
        {% endfor %}
    </urlset>

记得把网址换成自己的，另外`lastmod`节点表示此博文最后的更新时间，这样搜索引擎就可以根据这个时间更新快照了。
都添加完毕后，测试一下`http://127.0.0.1:8000/sitemap.xml`
网页中应该显示着你的所有博文生成的XML文件。









'''