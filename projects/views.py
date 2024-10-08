from django.shortcuts import render
from django.shortcuts import get_object_or_404


from projects.models import Project


def projects_list(request):
    projects = Project.objects.all()
    context = {"projects": projects}
    return render(request, "projects/projects-list.html", context)


def project_detail(request, slug):
    project = get_object_or_404(Project, slug=slug)
    context = {"project": project}
    return render(request, "projects/project-detail.html", context)
