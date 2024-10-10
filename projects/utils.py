from io import BytesIO
from pathlib import Path

from django.core.files import File
from PIL import Image

image_types = {
    "jpg": "JPEG",
    "jpeg": "JPEG",
    "png": "PNG",
    "gif": "GIF",
    "tif": "TIFF",
    "tiff": "TIFF",
}


def image_resize(image, width, height):
    # Open the image using Pillow
    img = Image.open(image)
    # check if either the width or height is greater than the max
    if img.width > width or img.height > height:
        output_size = (width, height)
        # Create a new resized “thumbnail” version of the image with Pillow
        img.thumbnail(output_size)
        # Find the file name of the image
        img_filename = Path(image.file.name).name
        # Spilt the filename on “.” to get the file extension only
        img_suffix = Path(image.file.name).name.split(".")[-1]
        # Use the file extension to determine the file type from the image_types dictionary
        img_format = image_types[img_suffix]
        # Save the resized image into the buffer, noting the correct file type
        buffer = BytesIO()
        img.save(buffer, format=img_format)
        # Wrap the buffer in File object
        file_object = File(buffer)
        # Save the new resized file as usual, which will save to S3 using django-storages
        image.save(img_filename, file_object)


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

    buffer = BytesIO()
    img.save(buffer, format=img_format)
    file_object = File(buffer)

    return file_object
