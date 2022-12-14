from django.urls import path
from . import views
from .views import home, DateView, BookingView, confirmed, view_bookings, delete_bookings

urlpatterns = [
    path('', home, name="home"),
    path('date/', DateView, name="date"),
    path('book/', BookingView, name="book"),
    path('confirmed/', confirmed, name="confirmed"),
    path('view_bookings/', view_bookings, name="view_bookings"),
    path('delete_bookings/<booking_id>',
         delete_bookings, name='delete_bookings'),
]
