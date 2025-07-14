from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import CustomUserCreationForm
from .models import Contact


# TODO реализуй свой метожд LOGIN !!!!!!!!!


# added required methods
# for example
# @require_http_methods(["POST"])
@login_required
def add_contact(request):
    # FIXME deprecated request.method for you 
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        email = request.POST.get("email")

        Contact.objects.create(user=request.user, name=name, phone=phone, email=email)
        messages.success(request, "Контакт успешно добавлен ✅")
        return redirect("contact_list")

    return render(request, "contacts/add_contact.html")

# added required methods
# for example
# @require_http_methods(["GET"])
def contact_list(request):
    contacts = Contact.objects.all()
    return render(request, "contacts/contact_list.html", {"contacts": contacts})

# added required methods
# for example
# @require_http_methods(["GET", "POST"])
def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(
                request, "Вы успешно зарегистрированы и вошли в аккаунт ✅"
            )
            return redirect("contact_list")
    else:
        form = CustomUserCreationForm()
    return render(request, "contacts/register.html", {"form": form})``
