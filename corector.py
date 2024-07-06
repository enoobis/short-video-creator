import os
from PIL import Image

def resize_images():
    # Get the path to the folder containing the images
    folder_path = os.path.join(os.getcwd(), "images")

    # Get a list of all the image filenames in the folder
    image_filenames = [f for f in os.listdir(folder_path) if f.endswith('.jpg')]

    # Get the dimensions of the first image in the folder
    first_image_path = os.path.join(folder_path, image_filenames[0])
    first_image = Image.open(first_image_path)
    first_image_width, first_image_height = first_image.size

    # Loop through the remaining images and resize them to match the dimensions of the first image
    for image_filename in image_filenames[1:]:
        image_path = os.path.join(folder_path, image_filename)
        image = Image.open(image_path)
        image_width, image_height = image.size
        if image_width != first_image_width or image_height != first_image_height:
            resized_image = image.resize((first_image_width, first_image_height))
            resized_image.save(image_path)
