from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def page1(request):
    msg="<h1>hello python!! welcome to page1!!</h1>"
    return HttpResponse(msg)