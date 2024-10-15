import io
from pathlib import Path

from django.core.files import File
from django.core.files.base import ContentFile
from PIL import Image

image_types = {
    "jpg": "JPEG",
    "jpeg": "JPEG",
    "png": "PNG",
    "gif": "GIF",
    "tif": "TIFF",
    "tiff": "TIFF",
}


def image_resize(image, max_width, max_height):
    with Image.open(image) as img:
        img.thumbnail((max_width, max_height))

        output = io.BytesIO()
        img.save(output, format="JPEG", quality=85)
        output.seek(0)

        return ContentFile(output.getvalue(), name=image.name)


def crop_image_16_9(image, max_width=512):
    img = Image.open(image)

    # Resize to max_width while maintaining aspect ratio
    img.thumbnail((max_width, max_width * 9 // 16), Image.LANCZOS)

    width, height = img.size
    target_height = width * 9 // 16

    # Crop to 16:9 aspect ratio
    left = 0
    top = (height - target_height) // 2
    right = width
    bottom = top + target_height
    img = img.crop((left, top, right, bottom))

    # Save the cropped image
    img_filename = Path(image.file.name).name
    img_suffix = img_filename.split(".")[-1]
    img_format = image_types[img_suffix]

    buffer = io.BytesIO()
    img.save(buffer, format=img_format)
    file_object = File(buffer)

    return file_object
