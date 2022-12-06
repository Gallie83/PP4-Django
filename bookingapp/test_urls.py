from django.test import SimpleTestCase
from django.urls import reverse, resolve
from bookingapp.views import home, DateView, BookingView, confirmed, view_bookings


class TestUrls(SimpleTestCase):

    # Tests Homepage Url is correct
    def test_home_url(self):
        url = reverse('home')
        self.assertEquals(resolve(url).func, home)

    # Tests DateView Url is correct
    def test_date_view_url(self):
        url = reverse('date')
        self.assertEquals(resolve(url).func, DateView)

    # Tests Homepage Url is correct
    def test_booking_view_url(self):
        url = reverse('book')
        self.assertEquals(resolve(url).func, BookingView)

    # Tests Confirmed Url is correct
    def test_confirmed_url(self):
        url = reverse('confirmed')
        self.assertEquals(resolve(url).func, confirmed)

    # Tests View Bookings Url is correct
    def test_view_bookings_url(self):
        url = reverse('view_bookings')
        self.assertEquals(resolve(url).func, view_bookings)
