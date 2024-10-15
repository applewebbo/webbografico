import tempfile

import pytest

from projects.test import TestCase
from tests.projects.factories import ImageFactory, ProjectFactory

pytestmark = pytest.mark.django_db


class TestProjectModel:
    def test_factory(self, project_factory):
        """Test detailed project factory"""

        project = project_factory(title="Test Project")

        assert project.__str__() == "Test Project"


class TestTechModel:
    def test_factory(self, tech_factory):
        """Test detailed tech factory"""

        tech = tech_factory(name="Test Tech")

        assert tech.__str__() == "Test Tech"


class ImageModelTestCase(TestCase):
    temporary_dir = None

    @classmethod
    def setUpClass(cls):
        cls.temporary_dir = tempfile.TemporaryDirectory()
        super().setUpClass()

    @classmethod
    def tearDownClass(cls):
        if cls.temporary_dir:
            cls.temporary_dir.cleanup()
        cls.temporary_dir = None
        super().tearDownClass()

    def test_factory(self):
        """Test detailed image factory"""
        with self.settings(MEDIA_ROOT=self.temporary_dir.name):
            project = ProjectFactory()
            image = ImageFactory(alt_text="Test Image", project=project)

            assert image.__str__() == "Test Image"

    def test_image_not_cropped_when_same_image_updated(self):
        """Test image is not cropped when it's the same image on an updated Image"""
        with self.settings(MEDIA_ROOT=self.temporary_dir.name):
            project = ProjectFactory()
            image = ImageFactory(alt_text="Original Image", project=project)

            original_image = image.image
            original_image_size = original_image.size

            # Update the image with the same file
            image.alt_text = "Updated Image"
            image.save()

            # Refresh from database
            image.refresh_from_db()

            # Check that the image hasn't changed
            assert image.image == original_image
            assert image.image.size == original_image_size
            assert image.alt_text == "Updated Image"
