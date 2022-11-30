from django.shortcuts import render
from .forms import DateForm, BookingForm
from django.shortcuts import redirect
from .models import Booking, Slots


# Renders home page
def home(request):
    return render(request, 'home.html', {})


# Renders page once user books a training session
def confirmed(request):
    return render(request, 'confirmed.html', {})

# Form that user chooses date for booking


def DateView(request):
    form = DateForm(request.POST or None)
    if form.is_valid():
        # Stores inputted date as string to be used in booking form
        request.session["dateSelected"] = str(
            form.cleaned_data["booking_date"])
        print(form.cleaned_data)

        # Redirects user to booking form page
        return redirect('book')

    context = {
        'form': form
    }
    return render(request, "date_form.html", context)

# Form user submits to reserve booking


def BookingView(request):
    # Retrieves date used in previous form and sets it to booking_date
    instance = Booking(booking_date=request.session.get(
        'dateSelected'), user=request.user)

    form = BookingForm(request.POST or None, instance=instance)

    if form.is_valid():

        print(form.cleaned_data)

        form.save()

        # Redirects user to booking form page
        return redirect('confirmed')

    context = {
        'form': form
    }
    return render(request, "booking_form.html", context)
