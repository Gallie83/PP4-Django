from django.test import SimpleTestCase
from bookingapp.forms import DateForm, BookingForm


class TestForms(SimpleTestCase):

    # Tests DateForm is valid
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

    # Tests BookingForm that slot is required
    def test_booking_form_valid_data(self):
        form = BookingForm({'slot': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('slot', form.errors.keys())
        self.assertEqual(form.errors['slot'][0], 'This field is required.')

    # Tests BookingForm is valid
    def test_booking_form_valid_data(self):
        form = BookingForm(data={
            'slot': '10.00 - 11.00',
        })

        self.assertTrue(form.is_valid())
