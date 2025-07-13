from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from contacts import views as contact_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("contacts.urls")),  # ⬅️ всё ок
    path("login/", auth_views.LoginView.as_view(template_name="contacts/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(next_page="contact_list"), name="logout"),
    path("register/", contact_views.register, name="register"),
]
