from django.urls import path
from . import views


urlpatterns = [
    path("", views.contact_list, name="contact_list"),
    path("add/", views.add_contact, name="add_contact"),
    path("register/", views.register, name="register"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
]
