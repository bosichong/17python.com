
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

#导入数据模型
from .models import Article

def index(request):
    return HttpResponse('你好，Django,江哥？')

def home(request):
    # s = 'Hello World!'
    # l = [1,2,3,4,5,6,7,8]
    # info_dict = {'h': 'hello', 'w': 'world'}

    articles = Article.objects.all()#获取所有文章数据
    return render(request, 'home.html', {'articles':articles,})
    
def blog(request,id):
    '''博客文章页面'''
    #首先通过文章的ID获得文章的所有数据,其中id为页面传递过来的参数。
    article = Article.objects.get(pk=id)#博文数据
    #传递数据到模板。
    return render(request, 'blog.html', {'article':article,})


def list(request):
    '''blog列表页'''
    #返回所有日志列表，以创建时间排序。
    articles = Article.objects.all().order_by('-create_time')
    print(articles)
    #把调用的数据传递给模板
    return render(request, 'list.html', {'articles':articles,})

