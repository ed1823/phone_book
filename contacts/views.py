from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .forms import CustomUserCreationForm
from .models import Contact


@login_required
def add_contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        email = request.POST.get("email")

        Contact.objects.create(user=request.user, name=name, phone=phone, email=email)
        messages.success(request, "Контакт успешно добавлен ✅")
        return redirect("contact_list")

    return render(request, "contacts/add_contact.html")


def contact_list(request):
    contacts = Contact.objects.all()
    return render(request, "contacts/contact_list.html", {"contacts": contacts})


def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # 👈 автоматически войти после регистрации
            messages.success(request, "Вы успешно зарегистрированы и вошли в аккаунт ✅")
            return redirect("contact_list")  # 👈 редирект на главную
    else:
        form = CustomUserCreationForm()
    return render(request, "contacts/register.html", {"form": form})
