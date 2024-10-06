# Generated by Django 5.1.1 on 2024-10-06 15:51

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
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
                ("image", models.ImageField(upload_to="img/projects/")),
                ("alt_text", models.CharField(max_length=100)),
            ],
        ),
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
                ("hero_image", models.ImageField(upload_to="img/projects/")),
                ("live_url", models.URLField()),
                ("source_code_url", models.URLField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "images",
                    models.ManyToManyField(
                        blank=True,
                        null=True,
                        related_name="projects",
                        to="projects.image",
                    ),
                ),
                (
                    "technologies",
                    models.ManyToManyField(
                        blank=True,
                        null=True,
                        related_name="projects",
                        to="projects.tech",
                    ),
                ),
            ],
        ),
    ]