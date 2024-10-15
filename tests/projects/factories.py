import factory
from django.core.files.base import ContentFile

from projects.models import Image, Project, Tech


class TechFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Tech

    name = factory.Faker("word")


class ProjectFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Project

    title = factory.Faker("sentence")
    slug = factory.Faker("slug")
    description = factory.Faker("paragraph")
    live_url = factory.Faker("url")
    source_code_url = factory.Faker("url")


class ImageFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Image

    image = factory.LazyAttribute(
        lambda _: ContentFile(
            factory.django.ImageField()._make_data({"width": 1024, "height": 768}),
            "example.jpg",
        )
    )
