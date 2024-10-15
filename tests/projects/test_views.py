from pytest_django.asserts import assertTemplateUsed

from projects.test import TestCase
from tests.projects.factories import ProjectFactory


class ProjectListView(TestCase):
    def test_get(self):
        ProjectFactory.create_batch(3)
        response = self.get("projects_list")

        self.response_200(response)
        assertTemplateUsed(response, "projects/projects-list.html")


class ProjectDetailView(TestCase):
    def test_get(self):
        project = ProjectFactory()
        response = self.get("project_detail", slug=project.slug)

        self.response_200(response)
        assertTemplateUsed(response, "projects/project-detail.html")
        assert response.context["project"] == project
