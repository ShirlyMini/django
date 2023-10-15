from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


# Create your views here.

def home(request):
    return render(request, 'authapp/index.html')


def signup(request):
    if request.method == "POST":
        user = request.POST["username"]
        email = request.POST["email"]
        pass1 = request.POST["pass1"]
        pass2 = request.POST["pass2"]

        myuser = User.objects.create_user(user, email, pass2)
        myuser.save()

        messages.success(request, "User added sucessfully")
        return redirect("/signin")

    return render(request, 'authapp/signup.html')


def signin(request):
    if request.method == "POST":
        myuser = request.POST["username"]
        pass1 = request.POST["pass1"]

        user = authenticate(username=myuser, password=pass1)
        if user is not None:
            login(request, user)
            return render(request, 'authapp/index.html', {"uname": myuser})
        else:
            messages.error(request, "Bad Credential")
            return redirect('/home')

    return render(request, 'authapp/signin.html')


def signout(request):
    logout(request)
    return redirect('/home')
