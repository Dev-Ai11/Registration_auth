from django.shortcuts import redirect, render, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from . import views

# @login_required(login_url='login')

def home(request):
    return render(request, "home.html", {})


def signup(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        passw = request.POST.get("password")
        pass2 = request.POST.get("confirm-password")

        if passw != pass2:
            return HttpResponse("please insert the right confirm password in both input" )
        else:
            my_user = User.objects.create_user(username, email, passw)
            my_user.save()
            return redirect("login")

    return render(request, "signup.html")


def login_user(request):
    if request.method== 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username = username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse('your user name and password is not correct')

    return render(request, "login.html")

def logout(request):
        logout(request)
        return redirect('login') 


