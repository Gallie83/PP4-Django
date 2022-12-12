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
