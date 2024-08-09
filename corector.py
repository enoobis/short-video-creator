""" the code resizes all .jpg images in the "images" 
 folder to match the dimensions of the first image in that folder"""

import os
from PIL import Image
def resize_images():
    folder_path = os.path.join(os.getcwd(), "images")
    image_filenames = [f for f in os.listdir(folder_path) if f.endswith('.jpg')]
    first_image_path = os.path.join(folder_path, image_filenames[0])
    first_image = Image.open(first_image_path)
    first_image_width, first_image_height = first_image.size

    for image_filename in image_filenames[1:]:
        image_path = os.path.join(folder_path, image_filename)
        image = Image.open(image_path)
        image_width, image_height = image.size
        if image_width != first_image_width or image_height != first_image_height:
            resized_image = image.resize((first_image_width, first_image_height))
            resized_image.save(image_path)
