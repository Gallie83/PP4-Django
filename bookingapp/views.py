from django.shortcuts import render
from .forms import DateForm, BookingForm
from django.shortcuts import redirect
from .models import Booking, Slots
from django.contrib import messages
from datetime import date
import datetime


# Renders home page
def home(request):
    return render(request, 'home.html', {})


# Renders page once user books a training session
def confirmed(request):
    return render(request, 'confirmed.html', {})


# Page where user can see their bookings
def view_bookings(request):
    # Prevents user from accessing page if not logged in
    if request.user.is_authenticated:
        # Only returns bookings made by user
        booking_list = Booking.objects.filter(user=request.user)

        return render(request, 'view_bookings.html',
                      {'booking_list': booking_list})

    # Brings user to log in page
    else:
        return redirect('login')


# Allows user to delete selected booking
def delete_bookings(request, booking_id):
    booking = Booking.objects.get(pk=booking_id)
    booking.delete()
    messages.success(request, ("Booking has been deleted!"))

    return redirect('view_bookings')


# Form that user chooses date for booking
def DateView(request):
    form = DateForm(request.POST or None)
    if form.is_valid():
        # Takes input and converts from str to date
        formDate = form.cleaned_data.get('booking_date')
        newDate = datetime.datetime.strptime(formDate, '%Y-%m-%d').date()
        # Checks if date is before current date and throws error message
        if newDate < date.today():
            messages.success(request, ("Invalid date selected!"))
            return redirect('date')
        else:
            # Stores inputted date as string to be used in booking form
            request.session["dateSelected"] = str(
                form.cleaned_data["booking_date"])

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

    # Searches database for all sessions booked on chosen date
    booked_slots = Booking.objects.filter(booking_date=request.session.get(
        'dateSelected')).values_list('slot', flat=True)

    available_slots = []

    # Stores available times on chosen date in available_slots
    for slot in Slots:
        if slot[0] not in booked_slots:
            print(slot)
            available_slots.append(slot[0])

    if form.is_valid():
        form.save()

        # Redirects user to confirmed booking page
        return redirect('confirmed')

    context = {
        'form': form,
        'available_slots': available_slots,
    }
    return render(request, "booking_form.html", context)
