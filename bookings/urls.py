from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('bookingapp.urls')),
    path('members/', include('django.contrib.auth.urls')),
    path('members/', include('members.urls')),
]

# 404 error page
handler404 = "helpers.views.handle_not_found"
