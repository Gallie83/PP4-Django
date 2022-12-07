from django.test import TestCase
from django.test import SimpleTestCase
from django.test.client import Client
from django.contrib.auth.models import User


class TestViews(SimpleTestCase):

    # Tests home page renders correct template
    def test_home_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

    # Tests confirmed page renders correct template
    def test_confirmed_page(self):
        response = self.client.get('/confirmed/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'confirmed.html')

    # Tests DateView page renders correct template
    def test_date_view_page(self):
        response = self.client.get('/date/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'date_form.html')


class TestViewsLogin(TestCase):

    # # Tests BookingView page renders correct template
    # def test_date_view_page(self):
    #     response = self.client.get('/book/')
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'booking_form.html')

    def setUp(self):
        self.client.force_login(
            User.objects.get_or_create(username='testuser')[0])

# def test_bookingview_adds_booking(self):
#     self.user = User.objects.create_user(
#         'john', 'lennon@thebeatles.com', 'johnlikestocode')
#     response = self.client.post('/book/', {
#         'slot': '10.00 - 11.00',
#         'booking_date': '2022-12-12'
#     })
#     self.assertRedirects(response, '/confirmed/')

# Tests view bookings page renders correct template
# def test_view_bookings_page(self):
#     response = self.client.get('/view_bookings/')
#     self.assertEqual(response.status_code, 200)
#     self.assertTemplateUsed(response, 'view_bookings.html')
