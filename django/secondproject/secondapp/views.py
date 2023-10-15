from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.

def currenttime(request):
    time = int(datetime.datetime.now().strftime('%H'))
    if time>12:
         msg = f"<h1>Hi!! Good evening</h1>"
    elif time<12:
        msg = f"<h1>Hi!! Good morning</h1>"
    else:
        msg = f"<h1>Hi!!</h1>"
    return HttpResponse(msg)