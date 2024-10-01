from django.shortcuts import render

from .forms import ContactForm


def index(request):
    return render(request, "core/index.html")


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "core/contact_success.html")
    else:
        form = ContactForm()
    return render(request, "core/contact.html", {"form": form})
