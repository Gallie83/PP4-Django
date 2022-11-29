from django.urls import path
from . import views
from .views import home, DateView

urlpatterns = [
    path('', home, name="home"),
    path('date/', DateView, name="date"),

]
