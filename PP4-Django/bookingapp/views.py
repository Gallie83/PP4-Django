from django.shortcuts import render
from .forms import DateForm, BookingForm


def home(request):
    return render(request, 'home.html', {})


def DateView(request):
    form = DateForm(request.POST or None)

    context = {
        'form': form
    }
    return render(request, "date_form.html", context)


def BookingView(request):
    form = BookingForm(request.POST or None)

    context = {
        'form': form
    }
    return render(request, "booking_form.html", context)
