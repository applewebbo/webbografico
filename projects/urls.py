from django.urls import path

from projects import views

urlpatterns = []

htmx_urlpatterns = [
    path("", views.projects_list, name="projects_list"),
]

urlpatterns += htmx_urlpatterns