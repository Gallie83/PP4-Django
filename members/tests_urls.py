from django.test import TestCase
from django.test import SimpleTestCase
from django.urls import reverse, resolve
from members.views import login_user, logout_user, register_user


class TestUrls(SimpleTestCase):

    # Tests Login User Url is correct
    def test_login_url(self):
        url = reverse('login')
        self.assertEquals(resolve(url).func, login_user)

    # Tests Logout User Url is correct
    def test_logout_user_url(self):
        url = reverse('logout')
        self.assertEquals(resolve(url).func, logout_user)

    # # Tests Register User Url is correct
    def test_register_user_url(self):
        url = reverse('register_user')
        self.assertEquals(resolve(url).func, register_user)
