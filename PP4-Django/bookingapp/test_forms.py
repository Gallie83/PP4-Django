from django.test import SimpleTestCase
from bookingapp.forms import DateForm, BookingForm


class TestForms(SimpleTestCase):

    # Tests DateForm
    def test_date_form_valid_data(self):
        form = DateForm(data={
            'user': 'admin',
            'slot': '10.00 - 11.00',
            'booking_date': '2022-12-12'
        })

        self.assertTrue(form.is_valid())

    def test_date_form_invalid_data(self):
        form = DateForm(data={})

        self.assertFalse(form.is_valid())
