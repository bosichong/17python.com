
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.db.models import Q#模糊查询多个字段使用
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger#翻页相关模块


from .forms import Searchform

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
    # 因为有分类文章数据的返回，这里的数据会被覆盖
    articles = Article.objects.all().order_by('-create_time')
    #通过request.GET.get('c', '')获取页面上的C的key，request.GET['c']也可以访问，但不安全。
    # 如果直接访问域名http://127.0.0.1:8000/访问没有值，这里可以把c的值设置为空，
    c = request.GET.get('c', '')
    if c:
        #搜索分类ID为c的所有文章，如果分类id为空，这里就返回所有文章。
        articles = articles.filter(category=c,).order_by('-create_time')

    #搜索结果数据
    s = ''#搜索关键字
    #以下判断表单是否验证成功，如果验证成功返回一个字符串s
    if request.method == 'GET':
        form = Searchform(request.GET)
        if form.is_valid():
            s = request.GET.get('s')
    if s :
        articles = articles.filter(Q(title__contains=s)|Q(content__contains=s)).order_by('-create_time')
    # print(c)
    # print(articles)
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

    
    #把调用的数据传递给模板
    return render(request, 'list.html', {'articles':articles, 'contacts':contacts,})

