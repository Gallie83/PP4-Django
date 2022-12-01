from django import forms
from .models import Booking
from datetime import date
from django.core.validators import MinValueValidator


class DateInput(forms.DateInput):
    input_type = 'date'


class DateForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = [
            'booking_date',
        ]
        widgets = {'booking_date': DateInput()}


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = [
            'user',
            'slot',
            'booking_date',
        ]

        widgets = {
            'booking_date': forms.HiddenInput(),
            'user': forms.HiddenInput(),
        }
