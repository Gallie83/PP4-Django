from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        # If user logs in successfully, redirect them to home page
        if user is not None:
            login(request, user)
            messages.success(request, ("You have logged in!."))
            return redirect('home')
        else:
            # Return an 'invalid login' error message.
            messages.success(request, ("Error logging in, please try again."))
            return redirect('login')

    else:
        return render(request, 'authenticate/login.html', {})


def logout_user(request):
    logout(request)
    messages.success(request, ("You have logged out."))
    return redirect('login')


def register_user(request):

    return render(request, 'authenticate/register_user.html', {})
