# Register your models here.
from django.contrib import admin

from projects.models import Image, Project, Tech
from projects.forms import CustomProjectForm


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    form = CustomProjectForm
    prepopulated_fields = {"slug": ("title",)}


@admin.register(Tech)
class TechAdmin(admin.ModelAdmin):
    pass


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    pass
