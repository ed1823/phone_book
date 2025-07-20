from django.contrib import admin
from django.urls import path

from phone_book import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.contact_list, name="contact_list"),
    path("add/", views.add_contact, name="add_contact"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("register/", views.register, name="register"),
]
