from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render, redirect

from .forms import ContactForm


def index(request):
    return render(request, "core/index.html")


def contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        name = form.cleaned_data["name"]
        email = form.cleaned_data["email"]
        message = form.cleaned_data["message"]
        send_mail(
            f"Contatto da {name} su webbografico.com",
            f"{message}\n\nRispondi a {email}",
            None,
            [settings.ADMIN_EMAIL],
            fail_silently=False,
        )
        messages.add_message(
            request,
            messages.SUCCESS,
            "Messaggio inviato con successo",
        )
        return redirect("index")

    context = {"form": form, "create": True}
    return render(request, "core/contact.html", context)
