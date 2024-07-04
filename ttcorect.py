import tkinter as tk
from PIL import Image
import os

def add_borders():
    # Get the folder path from the user
    folder_path = os.path.join(os.getcwd(), 'images')

    # Loop through each file in the folder
    for filename in os.listdir(folder_path):
        if filename.endswith('.jpg'):
            # Open the image
            image_path = os.path.join(folder_path, filename)
            image = Image.open(image_path)

            # Calculate the size of the new image with 16x9 aspect ratio
            width, height = image.size
            new_height = int(width / 9 * 16)

            # Calculate the size of the borders
            border_size = int((new_height - height) / 2)

            # Create a new image with black borders at the top and bottom
            new_image = Image.new('RGB', (width, new_height), (0, 0, 0))
            new_image.paste(image, (0, border_size))

            # Save the new image with the same filename
            new_image.save(os.path.join(folder_path, filename))
