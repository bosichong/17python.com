#codeing=utf-8
# @Time    : 2018-01-26
# @Author  : py.sky
# @Mail    : bosichong@qq.com
# @Site    : www.17python.com
# @Title   : 实战：利用Django开发部署自己的个人博客（16）博客分类后边显示分类文章数
# @Url     : http://www.17python.com/blog/67
# @Details : 实战：利用Django开发部署自己的个人博客（16）博客分类后边显示分类文章数
# @Other   : OS X 10.11.6
#            Python 3.6.1
#            PyCharm
###################################
# 实战：利用Django开发部署自己的个人博客（16）博客分类后边显示分类文章数
###################################

'''

通过之前教程的学习，你应该可以把博客部署上线的服务器上了，但是博客的功能依然很简单，这里我们继续丰富一下博客的功能。
假设我们需要在博客分类展示模块上加上每个分类下拥有的文章数，这个应该如何用Django实现呢？

## 需求分析

我们需要在博客分类展示模块上加上每个分类下拥有的文章数，这样可以让来访用户更直观的了解分类下文章的数目，具体效果如下：

![]()

如果需要知道每个分类下的文章数，需要知道分类的ID，然后在文章表中搜索统计所属此分类的文章即可知道当前分类的下的文章数。

+ 区得当前分类
+ 统计属于当前分类的文章数
+ 传送到前端展示


## 功能实现

当前分为的ID，这个在前端渲染中可以获得，那么如何二次传回获得分类文章总数呢？
还记得markdown的实现吗？对就是Django的自定义过滤器，

![](http://www.17python.com/media/upload/2017/12/Snip20171214_56.png)

先编写mytags.py过滤器代码：


    @register.filter
    def cat_count(cat_id):
        """统计分类下边的日志数"""
        return Article.objects.filter(article_category=cat_id).count()

上边的函数就是统计的核心代码，我们来看看，如何在前端渲染中引用

在base.html最顶上中引入`{% load mytags %}`

在分类显示那里添加代码

            <!-- 统计分类下文章数 -->
           <span class="am-badge am-align-right">{{ c.id|cat_count  }}</span>

我们运行服务器测试一下效果:

![]()

大功告成！只要这么简单的几行代码就搞定Django博客分类显示文章数

'''