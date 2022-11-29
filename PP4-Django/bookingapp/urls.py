from django.urls import path
from . import views
from .views import home, DateView, BookingView

urlpatterns = [
    path('', home, name="home"),
    path('date/', DateView, name="date"),
    path('book/', BookingView, name="book"),
]
