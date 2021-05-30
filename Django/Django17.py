#codeing=utf-8
# @Time    : 2018-02-07
# @Author  : py.sky
# @Mail    : bosichong@qq.com
# @Site    : www.17python.com
# @Title   : 实战：利用Django开发部署自己的个人博客（17）博客标签云随机显示
# @Url     : http://www.17python.com/blog/80
# @Details : 实战：利用Django开发部署自己的个人博客（17）博客标签云随机显示
# @Other   : OS X 10.11.6
#            Python 3.6.1
#            PyCharm
###################################
# 实战：利用Django开发部署自己的个人博客（17）博客标签云随机显示
###################################

'''

断断续续，`Django`博客实战教程进展很慢，也不知道有没有人看，最近身体有些不适休息了段时间，这几天刚刚有些恢复，看来人生还得继续。
人总是在不断的进步不断的思考不断的变化，前一阵觉得非常有意义感兴趣的事，曾过一段时间的沉淀就会有新的想法，或许某天，我会翻看之前写过的那些博文，
会不会有种冲动？我是谁，写了些什么？

不过人生还得继续，今天我们继续了解博客中云标签的实现，具体请看下图：


![]()


## 云标签需求

在写博客的时候我们通常会每篇博客定义一些标签，方便通过这些标签搜索到相关的博文，一般这些标签会在首页及文章下边展示，今天我们要实现的是全站显示的标签云。

## 云标签的实现

因为我们在录入文章的时候，已经输入了每篇文章的标签，我们只需要搜索出这些标签加以归纳，然后在需要的地方展示即可。
标签的存储应该有很多种方式，比较常见的有：保存为一张表，为每个标签定义相关的属性；另一种是只直接在文章表中定义为一个字段进行存储。
这里我采用的是第二种方式，在文章表中建了一个字段用来保存每篇文章的标签。

当前我们的博客中文章表里还没有标签这个字段，我们添加一下：

    tag = models.CharField(max_length=50, verbose_name=u'日志标签', default='')

然后更新一下数据库，添加更新一些标签一会要用到。如何更新数据库请参考之前的文章进行相关操作。

## 编写代码

我们有了数据，就可以进行统计筛选了，因为是全站显示，所以我们需要在`Django`的上下文管理器中进行代码编写。

1.首先获得所有文章中的标签数据

在上下文`blog_context.py`中编写代码：


    l = Article.objects.values("tag")#获得所有文章的标签
    tags = []#所有标签数据
    #清洗数据，把重复的去除
    for k in l :
        tlist = k["tag"].split(' ')
        for item in tlist:
            if item not in tags:
                tags.append(item)#加入list

    shuffle(tags)#重新洗牌，随机显示
    #定义TAGcss的样式，用来随机显示背景颜色
    tagcss =['am-radius','am-badge-primary','am-badge-secondary','am-badge-success','am-badge-warning','am-badge-danger']


这样，我们就把数据通过上下文管理员提交给前端了，然后我们在前端进行渲染。

## 前端渲染云标签

在`base.html` 右边导航中添加如下代码：

    <!-- 标签云 -->
      <section class="am-panel am-panel-default">
        <div class="am-panel-hd">标签云</div>
        <div class="am-panel-bd">
          {% for tag in alltags %}
          <a href="{% url '' %}?t={{ tag }}" class="am-badge {{ tagcss | random }}">{{ tag }}</a>
          {% endfor %}
        </div>
      </section>

刷新网页会看到如下效果：

![]()

其中`tagcss`使用过滤器随机显示背景颜色，不过细心的朋友会发现，点击当前标签页并没有显示相关的文章，因为我们还没有做好这个标签搜索。

## 实现标签连接显示相关文章

首先我们先建立一个`form`

在`forms.py`文件编写如下代码：

    class Tagform(forms.Form):
        """tag搜索表单"""
        t = forms.CharField(max_length=20)

这样我们就定义了一个表单。

接下来修改一下视图`views.py`文件中的代码,代码比较多具体请参考`Git`仓库中的源码。到目前为止，我们的标签连接可以正常使用了。

## 结尾

云标签这个功能很不错的，写起来稍有点麻烦，不过只要你了解了各部件的功能，就知道如何下手了。






'''