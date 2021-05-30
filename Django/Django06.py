#codeing=utf-8
# @Time    : 2017-11-29
# @Author  : J.sky
# @Mail    : bosichong@qq.com
# @Site    : www.17python.com
# @Title   : # 实战：利用Django开发部署自己的个人博客（6）Django整合前端框架Amaze UI
# @Url     : http://www.17python.com/blog/58
# @Details : # 实战：利用Django开发部署自己的个人博客（6）Django整合前端框架Amaze UI
# @Other   : OS X 10.11.6 
#            Python 3.6.1
#            VSCode 1.15.1
###################################
# 实战：利用Django开发部署自己的个人博客（6）Django整合前端框架Amaze UI
###################################

'''
上节，我们有了`Django admin`后台管理数据，我先通过后台添加一些数据，稍后我们将使用这些数据进行前端展示的测试。

## 前端的简单展示

还记得'http://127.0.0.1:8000/blog/home'这个页上渲染的内容不？我在03节的时候简单的了解一下Django模块的渲染。
这里我们尝试把这个页面渲染成blog的首页。
我们修改视图`myblog.views.py.home()`方法中的代码如下：

    articles = Article.objects.all()#获取所有文章数据
    return render(request, 'home.html', {'articles':articles,})

修改模板'home.html'中的代码：

    {% for art in articles %} 
        {{ art.id }}.{{ art.title }} -- {{ art.category }}<br>
        {{ art.content }}<br>
        ------------------------------------------------------<br>
    {% endfor %}

此时我们刷新一下页面查看：

![]()

这是一个丑陋的页面，我们不可能把这种页面做为自己的博客页面来发布的，那么我们需要美化一下我们的博客。

## 选择前端框架

如果把一个博客的那成分为三步：后台配置，前端美化，生产部署。
那么到目前为止，我们后端的配置及管理已经有了一个初步的框架了，当然数据库中的表及字段并不是完美的，后继我们还会根据自己的需要进行丰富。
现在我们把目录移动到网站的前端展示来，我们看看如果把我们的博客做的更漂亮些，风格更统一些。
前端的展示是访问博客的用户看的，用户会通过这些页面查看到博客内容，好的博客页面设计定会给人留下更多的印象。
所以把博客页面设计成风格统一又不失自己的个性就成了我们的一个新任务。

现在前端框架可以选择的实在是太多了，这里我就不做比较了，这次我选择用`Amaze UI`，一个国产的前端框架，
优点是文档比较全，兼容PC与无线端，使用起来方便简单，具体介绍请移步官方慢慢查看吧。

## 引入Amaze UI

关于妹子（Amaze UI）这里不过多的介绍，如果想具体的了解可以稳步到官方网站，她的文档做的还是比较详细的。
这里我们直接引入一个blog页面范例，通过这个例子我们直接套用Amaze UI框架，
[http://amazeui.org/examples/blog.html](http://amazeui.org/examples/blog.html)
打开这个页面后，我们分发现一个使用`Amaze UI`框架做好的`blog`页面，我们将以这个页为基础创建自己的页面了。
查看网页源码，复制所有代码备用，一会全部粘贴到自己的模板页中。

新建一个模板页，`myblog.templates.blog.html` ,粘贴刚刚复制的所有代码。
我们观察一下html代码，其中有三处需要我们更换一下地址，然后才能正常引用`Amaze UI`框架，

    <link rel="stylesheet" href="/css/amazeui.min.css"/>
    <script src="/js/jquery.min.js"></script>
    <script src="/js/amazeui.min.js"></script>

由于需要引入前端框架，虽然我们可以使用官方提供的CDN加速地址，但原则上推荐引用站点本地资源，这里就引发一个新的问题：网站静态资源地址。

## 静态资源目录

在项目的根目录下创建`static`这个目录，此目录与myblog目录同级，用来存放网站中所有静态文件。
修改配置文件`blog01.settings.py`:

    STATIC_URL = '/static/'
    STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]


应该默认就有这么一段设置代码，这段代码就是用来设置静态目录的，如果没有请添加上。
那么我们测试一下，随便在这个目录中创建一个文本或是复制来一张图片试试，这里我在static目录中创建了一个`test.txt`的文本。
启动Django的服务器，地址栏里输入：http://127.0.0.1:8000/static/test.txt

![]()

如果设置没有问题，上边文本就可以正常显示了。

## 修改前端框架引入文件目录

[下载Amaze UI](http://amazeui.org/getting-started#xia-zai-wen-jian),将包复制到静态文件的目录中解压，
更换模板中引文件的地址，修改后的代码如下：

    <link rel="stylesheet" href="/static/AmazeUI-2.7.2/assets/css/amazeui.min.css"/>
    <script src="/static/AmazeUI-2.7.2/assets/js/jquery.min.js"></script>
    <script src="/static/AmazeUI-2.7.2/assets/js/amazeui.min.js"></script>

其中框架中没有jq的文件，我们需要自己下载一个文件到静态目录中，下载地址：`http://libs.baidu.com/jquery/1.11.1/jquery.min.js`

到目前为止，前端框架在模板中的使用就配置好了，然后只需要编写视图、路由中的代码就可以继续测试了。

## 编写路由及视图代码

编写视图文件`views.py`,添加一个视图函数：`blog()`,代码如下：

    def blog(request,id):
        '''博客文章页面'''
        #首先通过文章的ID获得文章的所有数据,其中id为页面传递过来的参数。
        article = Article.objects.get(pk=id)#博文数据
        #传递数据到模板。
        return render(request, 'blog.html', {'article':article,})

这里的id参数很重要，是数据获得的入口，每个文章都会有一个Django自动生成的文章id，并且不重复，我们通过路由来获取这个id值。

编写urls.py路由代码:

    url(r'^blog/(?P<id>\w+)$', v.blog,),

这里我们只添加了一段代码，这段代码的含义如下：`^blog/ `表示以`blog/`为开头，`(?P<id>\w+)`$中，$表示结尾，()中的代码表示为一个参数，`\w+`,表示一个整数。
如果你对正则有些了解，看懂这段简短的代码是没有压力的。

修改模板`blog.html`代码：

    <article class="blog-main">
      <h3 class="am-article-title">
        <a href="#">{{ article.title }}</a>
      </h3>
      <h4 class="am-article-meta blog-meta">发布时间：2014/06/17</h4>

      <div class="am-g blog-content">
      {{ article.content }}
      </div>
    </article>

我们主要是修改`<article>`标签的代码，删除多余的`<article>`标签，只保留一个即可。
好了，至此博客文章页面的代码编写完成，我们测试一下，启动服务器：`python3 manage.py runserver `
地址栏里输入：`http://127.0.0.1:8000/blog/blog/1`

如果一切顺利，你会看到页面会渲染出来你自己添加的博客数据。至此我们的前端框架`Amaze UI`整合完毕。
结尾再啰嗦几句，`Amaze UI`框架自带的前端模块还是很丰富的，可以满足一个博客前后端的所有需求了，这里不打算再对`Amaze UI`进行更细致的讲解了。
因为我觉得官方的文档写的真的挺好，如果有更多的需要可以查阅官方文档进行学习。









'''