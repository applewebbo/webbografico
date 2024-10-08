from django.shortcuts import render
from django.shortcuts import get_object_or_404


from projects.models import Project


def projects_list(request):
    projects = Project.objects.all()
    context = {"projects": projects}
    return render(request, "projects/projects-list.html", context)


def project_detail(request, slug):
    qs = Project.objects.prefetch_related("images", "technologies")
    project = get_object_or_404(qs, slug=slug)
    context = {"project": project}
    return render(request, "projects/project-detail.html", context)
