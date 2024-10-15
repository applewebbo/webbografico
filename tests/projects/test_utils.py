import pytest
from io import BytesIO
from django.core.files import File
from PIL import Image
from projects.utils import image_resize, crop_image_16_9


@pytest.fixture
def test_image():
    image = Image.new("RGB", (800, 600), color="red")
    image_file = BytesIO()
    image.save(image_file, "JPEG")
    image_file.name = "test_image.jpg"
    image_file.seek(0)
    return File(image_file)


def test_image_resize(test_image):
    resized = image_resize(test_image, 400, 300)
    with Image.open(resized) as img:
        assert img.width <= 400
        assert img.height <= 300
        assert img.width < 800 or img.height < 600


def test_image_resize_no_change(test_image):
    original_image = Image.open(test_image)
    original_size = original_image.size

    image_resize(test_image, 1000, 1000)
    test_image.seek(0)
    resized_image = Image.open(test_image)

    assert resized_image.size == original_size


def test_crop_image_16_9(test_image):
    cropped_file = crop_image_16_9(test_image)
    cropped_image = Image.open(cropped_file)
    assert cropped_image.width / cropped_image.height == pytest.approx(16 / 9, rel=1e-2)


def test_crop_image_16_9_max_width(test_image):
    cropped_file = crop_image_16_9(test_image, max_width=400)
    cropped_image = Image.open(cropped_file)
    assert cropped_image.width <= 400
    assert cropped_image.width / cropped_image.height == pytest.approx(16 / 9, rel=1e-2)


def test_crop_image_16_9_small_image():
    small_image = Image.new("RGB", (100, 100), color="blue")
    small_file = BytesIO()
    small_image.save(small_file, "PNG")
    small_file.name = "small_image.png"
    small_file.seek(0)
    image = File(small_file)
    cropped_file = crop_image_16_9(image)
    cropped_image = Image.open(cropped_file)
    assert cropped_image.width / cropped_image.height == pytest.approx(16 / 9, rel=1e-2)
    assert cropped_image.width <= 100
