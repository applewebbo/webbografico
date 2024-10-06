from django.db import models


class Tech(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Image(models.Model):
    image = models.ImageField(upload_to="img/projects/")
    alt_text = models.CharField(max_length=100)


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    hero_image = models.ImageField(upload_to="img/projects/")
    images = models.ManyToManyField(
        Image, related_name="projects", blank=True, null=True
    )
    live_url = models.URLField()
    source_code_url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    technologies = models.ManyToManyField(
        Tech, related_name="projects", blank=True, null=True
    )

    def __str__(self):
        return self.title
