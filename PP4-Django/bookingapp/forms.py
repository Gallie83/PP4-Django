from django import forms
from .models import Booking


class DateInput(forms.DateInput):
    input_type = 'date'


class DateForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = [
            'booking_date',
        ]
        widgets = {'booking_date': DateInput()}
