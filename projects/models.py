from cloudinary.models import CloudinaryField
from django.core.exceptions import ValidationError
from django.core.files.uploadedfile import UploadedFile
from django.db import models

FILE_UPLOAD_MAX_MEMORY_SIZE = 1024 * 1024 * 2  # 2mb


def file_validation(file):
    if not file:
        raise ValidationError("No file selected.")

    if isinstance(file, UploadedFile):
        if file.size > FILE_UPLOAD_MAX_MEMORY_SIZE:
            raise ValidationError("File shouldn't be larger than 2MB.")


class Tech(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Technology"
        verbose_name_plural = "Technologies"

    def __str__(self):
        return self.name


class Image(models.Model):
    image = CloudinaryField(
        "image",
        use_filename=True,
        unique_filename=False,
        folder="webbografico/other_images",
        validators=[file_validation],
    )
    alt_text = models.CharField(max_length=100)
    title = models.CharField(max_length=100, blank=True)
    project = models.ForeignKey(
        "Project", on_delete=models.CASCADE, related_name="images"
    )

    def __str__(self):
        return self.alt_text

    def __unicode__(self):
        try:
            public_id = self.image.public_id
        except AttributeError:
            public_id = ""
        return f"Photo <{self.title}:{public_id}>"


class Project(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)
    short_desc = models.CharField(
        max_length=100,
        blank=True,
        help_text="This text will go in the project_list cards",
    )
    description = models.TextField(
        blank=True, help_text="This text will go in the project_detail page"
    )
    hero_image = CloudinaryField(
        "image",
        use_filename=True,
        unique_filename=False,
        folder="webbografico/hero_images",
        validators=[file_validation],
    )
    live_url = models.URLField()
    source_code_url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    technologies = models.ManyToManyField(Tech, related_name="projects", blank=True)

    def __str__(self):
        return self.title
