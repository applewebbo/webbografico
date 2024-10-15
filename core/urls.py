from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from core import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index, name="index"),
    path("contact/", views.contact, name="contact"),
    path("projects/", include("projects.urls")),
    path("__reload__/", include("django_browser_reload.urls")),
    path("tinymce/", include("tinymce.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
