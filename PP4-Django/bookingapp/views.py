from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'home.html', {})


def DateView(request):
    return render(request, "date_form.html", {})
