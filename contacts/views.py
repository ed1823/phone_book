from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .models import Contact


def contact_list(request):
    contacts = Contact.objects.all()
    return render(request, "contacts/contact_list.html", {"contacts": contacts})


@login_required
def add_contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        email = request.POST.get("email")

        Contact.objects.create(user=request.user, name=name, phone=phone, email=email)
        return redirect("contact_list")

    return render(request, "contacts/add_contact.html")
