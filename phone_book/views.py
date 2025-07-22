from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.db.models import Q
from django.shortcuts import redirect, render
from django.views.decorators.http import require_http_methods

from phone_book.forms import ContactForm, CustomUserCreationForm
from phone_book.models import Contact


@require_http_methods(["GET", "POST"])
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f"Пользователь {user.username} успешно вошёл ✅")
            return redirect("contact_list")
        else:
            messages.error(request, "Некорректное имя пользователя или пароль")
    else:
        form = AuthenticationForm()

    return render(request, "contacts/login.html", {"form": form})


@login_required
def logout_view(request):
    logout(request)
    messages.success(request, "Выход успешно выполнен")
    return redirect("login")


@require_http_methods(["GET", "POST"])
@login_required
def add_contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.user = request.user
            contact.save()
            messages.success(request, "Контакт успешно добавлен")
            return redirect("contact_list")
        else:
            messages.error(request, "Проверьте форму на ошибки")
    else:
        form = ContactForm()

    return render(request, "contacts/add_contact.html", {"form": form})


@require_http_methods(["GET"])
def contact_list(request):
    search = request.GET.get("search", "")
    sort = request.GET.get("sort", "name")

    reverse_sort = sort.startswith("-")
    base_sort = sort.lstrip("-")

    contacts = Contact.objects.all()

    if search:
        contacts = contacts.filter(
            Q(name__icontains=search)
            | Q(phone__icontains=search)
            | Q(email__icontains=search)
        )
    contacts = contacts.order_by(
        sort
    )  # TODO изучить как работает order_by и доработать адекватно на фронте

    return render(
        request,
        "contacts/contact_list.html",
        {
            "contacts": contacts,
            "query": search,
            "sort": base_sort,
            "reverse_sort": reverse_sort,
        },
    )


@require_http_methods(["GET", "POST"])
def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Вы успешно зарегистрированы и вошли в систему")
            return redirect("contact_list")
    else:
        form = CustomUserCreationForm()

    return render(request, "contacts/register.html", {"form": form})
