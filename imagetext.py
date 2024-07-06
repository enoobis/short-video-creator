import os
from PIL import Image, ImageDraw, ImageFont

# Set base path as the current working directory
base_path = os.getcwd()

# Set relative paths for the text, image, output folders, and font file
text_folder = os.path.join(base_path, 'text')
image_folder = os.path.join(base_path, 'images')
output_folder = os.path.join(base_path, 'text-images')
font_path = os.path.join(base_path, 'font', 'font2.ttf')

# Define function to add text to images
def add_text_to_images():
    # Loop through text files in the text folder and corresponding images in the image folder
    for text_file, image_file in zip(sorted(os.listdir(text_folder)), sorted(os.listdir(image_folder))):
        # Construct the full path to the image
        img_path = os.path.join(image_folder, image_file)
        
        # Open the image
        with Image.open(img_path) as img:
            # Get the image dimensions
            width, height = img.size

            # Construct the full path to the text file
            txt_path = os.path.join(text_folder, text_file)
            
            # Open and read the text file
            with open(txt_path, 'r') as f:
                text = f.read()

            # Set font size relative to the image dimensions
            font_size = int(min(width, height) * 0.08)
            
            # Load the specified font
            font = ImageFont.truetype(font_path, font_size)

            # Create a drawing context
            draw = ImageDraw.Draw(img)

            # Calculate the dimensions of the text
            text_width, text_height = draw.textsize(text, font=font)

            # Check if the text fits within the image dimensions
            if text_width <= width and text_height <= height:
                # Calculate position to center the text
                x = (width - text_width) // 2
                y = (height - text_height) // 2
                
                # Add the text to the image
                draw.text((x, y), text, font=font, fill=(255, 255, 255))
            else:
                # Split the text into lines to fit within the image
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

                # Calculate the total height of the text block
                text_height = len(lines) * text_height
                y = (height - text_height) // 2
                
                # Add each line to the image
                for line in lines:
                    line_width, line_height = draw.textsize(line, font=font)
                    x = (width - line_width) // 2
                    draw.text((x, y), line, font=font, fill=(255, 255, 255))
                    y += line_height

            # Construct the output path
            output_path = os.path.join(output_folder, image_file)
            
            # Save the output image with the text added
            img.save(output_path)