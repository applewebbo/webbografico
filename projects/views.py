from django.shortcuts import render

from projects.models import Project


def projects_list(request):
    projects = Project.objects.all().prefetch_related("technologies")
    return render(request, "projects/projects-list.html", {"projects": projects})
