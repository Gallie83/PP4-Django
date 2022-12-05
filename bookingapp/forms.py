from django import forms
from .models import Booking


# Nicer style for Date Picker
class DateInput(forms.DateInput):
    input_type = 'date'


# Form for user to choose date of session
class DateForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = [
            'booking_date',
        ]
        widgets = {'booking_date': DateInput()}


# Form for user to choose time of session
class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = [
            'user',
            'slot',
            'booking_date',
        ]

    # Hides user and booking_date fields for a cleaner look
        widgets = {
            'booking_date': forms.HiddenInput(),
            'user': forms.HiddenInput(),
        }
