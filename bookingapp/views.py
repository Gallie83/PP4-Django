from django.shortcuts import render
from .forms import DateForm, BookingForm
from django.shortcuts import redirect
from .models import Booking, Slots
from django.contrib.auth.decorators import login_required
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

        past_booking_list = []

        upcoming_booking_list = []

    # Iterates through list and converts date from a string to a date
        for session in booking_list:
            sessionDate = session.booking_date
            newDate = datetime.datetime.strptime(
                sessionDate, '%Y-%m-%d').date()
            # Checks to see if date is a past date
            if newDate < date.today():
                past_booking_list.append(session)
            else:
                upcoming_booking_list.append(session)

        context = {'booking_list': booking_list,
                   'past_booking_list': past_booking_list,
                   'upcoming_booking_list': upcoming_booking_list}

        return render(request, 'view_bookings.html', context)

    # Brings user to log in page
    else:
        return redirect('login')


# Form that user chooses date for booking
def DateView(request):
    form = DateForm(request.POST or None)
    if form.is_valid():
        # Takes input and converts from str to date
        formDate = form.cleaned_data.get('booking_date')
        print(formDate)
        newDate = datetime.datetime.strptime(formDate, '%Y-%m-%d').date()
        print(newDate)
        # Checks if date is before current date and throws error message
        if newDate < date.today():
            messages.success(request, ("Invalid date selected!"))
            return redirect('date')
        # Stops user from making a booking on todays date
        elif newDate == date.today():
            messages.success(
                request, ("Sessions must be booked at least a day in advance!"))
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


def edit_date(request, booking_id):
    old_booking = Booking.objects.get(pk=booking_id)
    old_booking_pk = booking_id

    form = DateForm(request.POST or None)
    if form.is_valid():
        # Takes input and converts from str to date
        formDate = form.cleaned_data.get('booking_date')
        newDate = datetime.datetime.strptime(formDate, '%Y-%m-%d').date()
        # Checks if date is before current date and throws error message
        if newDate < date.today():
            messages.success(request, ("Invalid date selected!"))
            return redirect('date')
        # Stops user from making a booking on todays date
        elif newDate == date.today():
            messages.success(
                request, ("Sessions must be booked at least a day in advance!"))
            return redirect('date')
        else:
            # Stores inputted date as string to be used in booking form
            request.session["dateSelected"] = str(
                form.cleaned_data["booking_date"])
            # Stores old booking data in session
            request.session["oldBooking"] = str(old_booking)
            request.session["oldBookingPk"] = str(old_booking_pk)

            # Redirects user to booking form page
            return redirect('edit_booking')

    context = {
        'old_booking': old_booking,
        'old_booking_pk': old_booking_pk,
        'form': form
    }
    return render(request, 'edit_date_form.html', context)


def edit_booking(request):
    # Retrieves date used in previous form and sets it to booking_date
    instance = Booking(booking_date=request.session.get(
        'dateSelected'), user=request.user)

    # Gets previous booking data
    old_booking = request.session.get("oldBooking")
    print(old_booking)
    old_booking_pk = request.session.get("oldBookingPk")

    form = BookingForm(request.POST or None, instance=instance)

    # Searches database for all sessions booked on chosen date
    booked_slots = Booking.objects.filter(booking_date=request.session.get(
        'dateSelected')).values_list('slot', flat=True)

    available_slots = []

    # Stores available times on chosen date in available_slots
    for slot in Slots:
        if slot[0] not in booked_slots:
            available_slots.append(slot[0])

    if form.is_valid():
        form.save()
        # Once new booking is made, remove old booking
        previous_booking = Booking.objects.get(pk=old_booking_pk)
        previous_booking.delete()
        # Redirects user to confirmed booking page
        return redirect('edit_confirmed')

    context = {
        'form': form,
        'available_slots': available_slots,
        'old_booking': old_booking,
    }
    return render(request, "edit_booking_form.html", context)

# Renders page once user edits a session


def edit_confirmed(request):
    return render(request, 'edit_confirmed.html', {})


# Allows user to delete selected booking
@login_required
def delete_bookings(request, booking_id):
    booking = Booking.objects.get(pk=booking_id)
    booking.delete()
    messages.success(request, ("Booking has been deleted!"))

    return redirect('view_bookings')
