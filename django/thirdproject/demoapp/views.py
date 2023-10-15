from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
#print(__file__)
#import os

#print(os.path.dirname(os.path.dirname(__file__)))

def display(request):
    time = datetime.now()
    dict1={"display_time": time, "course":"django", "batch": "evening batch"}
    return render(request, 'demoapp/index1.html', context=dict1)
