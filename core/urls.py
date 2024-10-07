from django.contrib import admin
from django.urls import path, include

from core import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index, name="index"),
    path("contact/", views.contact, name="contact"),
    path("projects/", include("projects.urls")),
    path("__reload__/", include("django_browser_reload.urls")),
    path("tinymce/", include("tinymce.urls")),
]
