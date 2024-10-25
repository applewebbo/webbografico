import factory

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

    project = factory.SubFactory(ProjectFactory)
