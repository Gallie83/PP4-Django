from django.urls import path
from . import views

# Split into 2 lines to prevent pep validation error
from .views import home, DateView, BookingView, confirmed, edit_date
from .views import edit_booking, edit_confirmed, view_bookings, delete_bookings

urlpatterns = [
    path('', home, name="home"),
    path('date/', DateView, name="date"),
    path('book/', BookingView, name="book"),
    path('confirmed/', confirmed, name="confirmed"),
    path('view_bookings/', view_bookings, name="view_bookings"),
    path('edit_date/<booking_id>',
         edit_date, name='edit_date'),
    path('edit_booking/', edit_booking, name="edit_booking"),
    path('edit_confirmed/', edit_confirmed, name="edit_confirmed"),
    path('delete_bookings/<booking_id>',
         delete_bookings, name='delete_bookings'),
]
