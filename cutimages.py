import os
from PIL import Image

# set the path to your image folder
path = r"C:\Users\enoobis\Desktop\video-project\images"

# define a function to process the images
def process_images():
    # loop through each file in the folder
    for i, filename in enumerate(os.listdir(path)):
        # check if the file is a jpeg image
        if filename.endswith(".jpg") or filename.endswith(".jpeg"):
            # open the image file
            image_path = os.path.join(path, filename)
            with Image.open(image_path) as img:
                # crop the image to 1x1
                width, height = img.size
                crop_size = min(width, height)
                left = (width - crop_size) // 2
                top = (height - crop_size) // 2
                right = left + crop_size
                bottom = top + crop_size
                img_cropped = img.crop((left, top, right, bottom))
                # save the cropped image with a new filename
                new_filename = str(i+1) + ".jpg"
                img_cropped.save(os.path.join(path, new_filename))


