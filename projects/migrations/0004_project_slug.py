# Generated by Django 5.1.1 on 2024-10-08 06:21

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("projects", "0003_alter_tech_options_alter_project_hero_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="project",
            name="slug",
            field=models.SlugField(default="test", max_length=100),
            preserve_default=False,
        ),
    ]
