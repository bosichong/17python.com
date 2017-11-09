
from django.http import HttpResponse, HttpResponseRedirect

def index(request):
    return HttpResponse('你好，Django,江哥？')