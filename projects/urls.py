from django.urls import path

from projects import views

urlpatterns = [
    path("<slug:slug>/", views.project_detail, name="project_detail"),
]

htmx_urlpatterns = [
    path("", views.projects_list, name="projects_list"),
]

urlpatterns += htmx_urlpatterns
