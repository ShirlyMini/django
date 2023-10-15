from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def page1(request):
    msg="<h1>hello python!! welcome to page1!!</h1>"
    return HttpResponse(msg)

def page2(request):
    msg="<h1>hello python!! welcome to page2!!</h1>"
    return HttpResponse(msg)

def page3(request):
    msg="<h1>hello python!! welcome to page3!!</h1>"
    return HttpResponse(msg)