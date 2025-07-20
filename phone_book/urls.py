from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include, path

from contacts import views as contact_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("contacts.urls")),
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="contacts/login.html"),
        name="login",
    ),
    path(
        "logout/",
        auth_views.LogoutView.as_view(next_page="contact_list"),
        name="logout",
    ),
    path("register/", contact_views.register, name="register"),
    path("", contact_views.contact_list, name="contact_list"),
    path("add/", contact_views.add_contact, name="add_contact"),
    path("login/", contact_views.login_view, name="login"),
    path("logout/", contact_views.logout_view, name="logout"),
    path("register/", contact_views.register, name="register"),
]
