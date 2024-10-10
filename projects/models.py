from django.db import models

from projects.utils import image_resize


class Tech(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Technology"
        verbose_name_plural = "Technologies"

    def __str__(self):
        return self.name


class Image(models.Model):
    image = models.ImageField(upload_to="img/projects/")
    alt_text = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        image_resize(self.image, 512, 512)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.alt_text


class Project(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    description = models.TextField()
    hero_image = models.ImageField(upload_to="img/projects/", default="img/website.png")
    images = models.ManyToManyField(Image, related_name="projects", blank=True)
    live_url = models.URLField()
    source_code_url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    technologies = models.ManyToManyField(Tech, related_name="projects", blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.hero_image:
            image_resize(self.hero_image, 1024, 512)
        super().save(*args, **kwargs)
