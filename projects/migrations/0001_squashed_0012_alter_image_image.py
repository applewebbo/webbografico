# Generated by Django 5.1.2 on 2024-10-25 12:50

import cloudinary.models
import django.db.models.deletion
import projects.models
from django.db import migrations, models


class Migration(migrations.Migration):
    replaces = [
        ("projects", "0001_initial"),
        ("projects", "0002_alter_project_images_alter_project_technologies"),
        ("projects", "0003_alter_tech_options_alter_project_hero_image"),
        ("projects", "0004_project_slug"),
        ("projects", "0005_remove_project_images_image_project"),
        ("projects", "0006_image_title"),
        ("projects", "0007_alter_project_hero_image"),
        ("projects", "0008_alter_project_hero_image"),
        ("projects", "0009_alter_image_image"),
        ("projects", "0010_alter_image_image_alter_project_hero_image"),
        ("projects", "0011_alter_project_hero_image"),
        ("projects", "0012_alter_image_image"),
    ]

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Tech",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
            ],
            options={
                "verbose_name": "Technology",
                "verbose_name_plural": "Technologies",
            },
        ),
        migrations.CreateModel(
            name="Project",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=100)),
                ("description", models.TextField()),
                (
                    "hero_image",
                    cloudinary.models.CloudinaryField(
                        max_length=255,
                        validators=[projects.models.file_validation],
                        verbose_name="image",
                    ),
                ),
                ("live_url", models.URLField()),
                ("source_code_url", models.URLField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "technologies",
                    models.ManyToManyField(
                        blank=True, related_name="projects", to="projects.tech"
                    ),
                ),
                ("slug", models.SlugField(default="test", max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Image",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "image",
                    cloudinary.models.CloudinaryField(
                        max_length=255,
                        validators=[projects.models.file_validation],
                        verbose_name="image",
                    ),
                ),
                ("alt_text", models.CharField(max_length=100)),
                (
                    "project",
                    models.ForeignKey(
                        default=1,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="images",
                        to="projects.project",
                    ),
                ),
                ("title", models.CharField(blank=True, max_length=100)),
            ],
        ),
    ]
