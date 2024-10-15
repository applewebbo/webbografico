from pytest_factoryboy import register

from tests.core.factories import UserFactory
from tests.projects.factories import ProjectFactory, TechFactory, ImageFactory

register(UserFactory)
register(ProjectFactory)
register(TechFactory)
register(ImageFactory)
