# Generated by Django 5.1.2 on 2024-10-17 06:47

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("projects", "0006_image_title"),
    ]

    operations = [
        migrations.AlterField(
            model_name="project",
            name="hero_image",
            field=models.ImageField(
                default="img/projects/website.jpg", upload_to="img/projects/"
            ),
        ),
    ]
