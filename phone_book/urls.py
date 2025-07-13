from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('contacts.urls')),
    path('auth/', include('django.contrib.auth.urls')),  # login, logout
]
