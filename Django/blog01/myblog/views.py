
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

def index(request):
    return HttpResponse('你好，Django,江哥？')

def home(request):
    s = 'Hello World!'
    l = [1,2,3,4,5,6,7,8]
    info_dict = {'h': 'hello', 'w': 'world'}
    return render(request, 'home.html', {'s':s, 'l':l, 'info_dict':info_dict})
    