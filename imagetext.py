import os
from PIL import Image, ImageDraw, ImageFont

# Set paths
text_folder = r'C:\Users\enoobis\Desktop\video-project\text'
image_folder = r'C:\Users\enoobis\Desktop\video-project\images'
output_folder = r'C:\Users\enoobis\Desktop\video-project\text-images'
font_path = r'C:\Users\enoobis\Desktop\video-project\font\font2.ttf'

# Define function to execute script
def add_text_to_images():
    # Loop through text files in text folder and corresponding images in image folder
    for text_file, image_file in zip(sorted(os.listdir(text_folder)), sorted(os.listdir(image_folder))):
        # Open image
        img_path = os.path.join(image_folder, image_file)
        with Image.open(img_path) as img:
            # Get image dimensions
            width, height = img.size

            # Open text file
            txt_path = os.path.join(text_folder, text_file)
            with open(txt_path, 'r') as f:
                text = f.read()

            # Set font size and load font
            font_size = int(min(width, height) * 0.08)
            font = ImageFont.truetype(font_path, font_size)

            # Create drawing context
            draw = ImageDraw.Draw(img)

            # Calculate text dimensions
            text_width, text_height = draw.textsize(text, font=font)

            # Check if text fits within image
            if text_width <= width and text_height <= height:
                # Add text to image
                x = (width - text_width) // 50
                y = (height - text_height) // 50
                draw.text((x, y), text, font=font, fill=(255, 255, 255))
            else:
                # Split text into lines
                words = text.split()
                lines = []
                current_line = words[0]
                for word in words[1:]:
                    test_line = current_line + ' ' + word
                    test_width, test_height = draw.textsize(test_line, font=font)
                    if test_width <= width:
                        current_line = test_line
                    else:
                        lines.append(current_line)
                        current_line = word
                lines.append(current_line)

                # Add lines to image
                text_height = len(lines) * text_height
                y = (height - text_height) // 50
                for line in lines:
                    line_width, line_height = draw.textsize(line, font=font)
                    x = (width - line_width) // 50
                    draw.text((x, y), line, font=font, fill=(255, 255, 255))
                    y += line_height

            # Save output image
            output_path = os.path.join(output_folder, image_file)
            img.save(output_path)