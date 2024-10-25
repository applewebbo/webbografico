import pytest
from django.core.exceptions import ValidationError
from django.core.files.uploadedfile import SimpleUploadedFile
from projects.test import TestCase


from projects.models import FILE_UPLOAD_MAX_MEMORY_SIZE, file_validation
from tests.projects.factories import ImageFactory, ProjectFactory

pytestmark = pytest.mark.django_db


class TestProjectModel:
    def test_factory(self, project_factory):
        """Test detailed project factory"""

        project = project_factory(title="Test Project")

        assert project.__str__() == "Test Project"


class TestTechModel:
    def test_tech_factory(self, tech_factory):
        """Test detailed tech factory"""

        tech = tech_factory(name="Test Tech")

        assert tech.__str__() == "Test Tech"


class ImageModelTest(TestCase):
    def test_image_factory(self):
        project = ProjectFactory()
        image = ImageFactory(alt_text="Sample Alt Text", project=project)
        assert image.__str__() == "Sample Alt Text"

    def test_image_unicode(self):
        project = ProjectFactory()
        image = ImageFactory(title="Sample Title", project=project)
        assert image.__unicode__() == "Photo <Sample Title:>"


class FileValidationTest(TestCase):
    def test_file_validation_no_file(self):
        with self.assertRaisesMessage(ValidationError, "No file selected."):
            file_validation(None)

    def test_file_validation_file_too_large(self):
        large_file = SimpleUploadedFile(
            "large_file.txt", b"x" * (FILE_UPLOAD_MAX_MEMORY_SIZE + 1)
        )
        with self.assertRaisesMessage(
            ValidationError, "File shouldn't be larger than 2MB."
        ):
            file_validation(large_file)

    def test_file_validation_valid_file(self):
        valid_file = SimpleUploadedFile(
            "valid_file.txt", b"x" * (FILE_UPLOAD_MAX_MEMORY_SIZE - 1)
        )
        try:
            file_validation(valid_file)
        except ValidationError:
            self.fail("file_validation raised ValidationError unexpectedly!")

    def test_file_validation_non_uploadedfile(self):
        non_uploaded_file = "This is not an UploadedFile object"
        try:
            file_validation(non_uploaded_file)
        except ValidationError:
            self.fail("file_validation raised ValidationError unexpectedly!")
