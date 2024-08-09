"""the code adds text from files in the "text" folder to corresponding images in the "images" folder.
it uses a specified font and saves the resulting images with text to the "text-images" folder."""


import os
from PIL import Image, ImageDraw, ImageFont

base_path = os.getcwd()

text_folder = os.path.join(base_path, 'text')
image_folder = os.path.join(base_path, 'images')
output_folder = os.path.join(base_path, 'text-images')
font_path = os.path.join(base_path, 'font', 'font2.ttf')

def add_text_to_images():
    for text_file, image_file in zip(sorted(os.listdir(text_folder)), sorted(os.listdir(image_folder))):
        img_path = os.path.join(image_folder, image_file)
        
        with Image.open(img_path) as img:
            width, height = img.size
            txt_path = os.path.join(text_folder, text_file)
            
            with open(txt_path, 'r') as f:
                text = f.read()

            font_size = int(min(width, height) * 0.08)
            font = ImageFont.truetype(font_path, font_size)
            draw = ImageDraw.Draw(img)

            x = 0
            y = 10 
            
            words = text.split()
            lines = []
            current_line = words[0]
            for word in words[1:]:
                test_line = current_line + ' ' + word
                bbox = draw.textbbox((0, 0), test_line, font=font)
                test_width = bbox[2] - bbox[0]
                if test_width <= width:
                    current_line = test_line
                else:
                    lines.append(current_line)
                    current_line = word
            lines.append(current_line)

            for line in lines:
                bbox = draw.textbbox((0, 0), line, font=font)
                line_width = bbox[2] - bbox[0]
                x = (width - line_width) // 2
                draw.text((x, y), line, font=font, fill=(255, 255, 255))
                y += bbox[3] - bbox[1]

            output_path = os.path.join(output_folder, image_file)
            img.save(output_path)
