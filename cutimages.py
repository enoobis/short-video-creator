"""the code crops .jpg and .jpeg images to 1x1 squares
 and saves them in the same folder"""

import os
from PIL import Image

path = os.path.join(os.getcwd(), "images")

def process_images():
    for i, filename in enumerate(os.listdir(path)):
        if filename.endswith(".jpg") or filename.endswith(".jpeg"):
            image_path = os.path.join(path, filename)
            with Image.open(image_path) as img:
                width, height = img.size
                crop_size = min(width, height)
                left = (width - crop_size) // 2
                top = (height - crop_size) // 2
                right = left + crop_size
                bottom = top + crop_size
                img_cropped = img.crop((left, top, right, bottom))
                new_filename = str(i+1) + ".jpg"
                img_cropped.save(os.path.join(path, new_filename))


