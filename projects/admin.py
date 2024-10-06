# Register your models here.
from django.contrib import admin
from projects.models import Project, Tech, Image


@admin.register(Project)
class SchoolAdmin(admin.ModelAdmin):
    pass


@admin.register(Tech)
class TechAdmin(admin.ModelAdmin):
    pass


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    pass
