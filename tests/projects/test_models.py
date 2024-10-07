from django.test import TestCase

from projects.models import Project, Tech


class ProjectModelTestCase(TestCase):
    def setUp(self):
        self.project = Project.objects.create(
            title="Test Project", description="This is a test project"
        )

    def test_project_str(self):
        self.assertEqual(str(self.project), "Test Project")


class TechModelTestCase(TestCase):
    def setUp(self):
        self.tech = Tech.objects.create(
            name="Test Task",
        )

    def test_task_str(self):
        expected_str = "Test Task"
        self.assertEqual(str(self.tech), expected_str)
