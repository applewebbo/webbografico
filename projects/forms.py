from django import forms
from django.db import models

from projects.models import Project


def urlfields_assume_https(db_field, **kwargs):
    """
    ModelForm.Meta.formfield_callback function to assume HTTPS for scheme-less
    domains in URLFields.
    """
    if isinstance(db_field, models.URLField):
        kwargs["assume_scheme"] = "https"
    return db_field.formfield(**kwargs)


class CustomProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = "__all__"
        help_texts = {
            "hero_image": "Please, upload an image with a resolution of 1280x720",
        }
        formfield_callback = urlfields_assume_https
