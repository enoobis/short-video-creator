"""the code adds black borders to .jpg images in the "images" folder
 to convert them to a 16:9 aspect ratio."""

import tkinter as tk
from PIL import Image
import os

def add_borders():
    folder_path = os.path.join(os.getcwd(), 'images')

    for filename in os.listdir(folder_path):
        if filename.endswith('.jpg'):
            image_path = os.path.join(folder_path, filename)
            image = Image.open(image_path)
            width, height = image.size
            new_height = int(width / 9 * 16)
            border_size = int((new_height - height) / 2)
            new_image = Image.new('RGB', (width, new_height), (0, 0, 0))
            new_image.paste(image, (0, border_size))
            new_image.save(os.path.join(folder_path, filename))
