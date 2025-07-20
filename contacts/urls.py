from django.urls import path
from contacts import views as contact_views

urlpatterns = [
    path("", contact_views.contact_list, name="contact_list"),
    path("add/", contact_views.add_contact, name="add_contact"),
    path("login/", contact_views.login_view, name="login"),
    path("logout/", contact_views.logout_view, name="logout"),
    path("register/", contact_views.register, name="register"),
]
