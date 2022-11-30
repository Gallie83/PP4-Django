from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm


# View for user to login
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


# View for user to logout
def logout_user(request):
    logout(request)
    # Logs user out and redirects them to login page with logout message
    messages.success(request, ("You have logged out."))
    return redirect('login')


# View for new users to register
def register_user(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "Registration Successful!")
            return redirect('home')
    else:
        form = UserCreationForm()

    return render(request, 'authenticate/register_user.html', {'form': form, })
