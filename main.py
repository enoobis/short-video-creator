import tkinter as tk
import customtkinter
import json
import os

from deleteall import *
from images import *
from voice import *
from cvideo import *
from video import *
from cutimages import *
from ttcorect import *
from imagetext import *
from musicvideo import *
from corector import *

from tkinter import filedialog
from PIL import Image, ImageDraw, ImageFont

# Theme for Tkinter
customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green


def save_all_images_and_mp3(image_entries, text_entries):
    for i in range(5):
        download_image(image_entries[i].get())
        save_as_mp3(text_entries[i].get("1.0", "end-1c"))
        with open(os.path.join('C:\\Users\\enoobis\\Desktop\\video-project\\text', f'{i+1}.txt'), 'w') as f:
            f.write(text_entries[i].get("1.0", "end-1c"))
            label.config(text="operation = successful")

# GUI
root = customtkinter.CTk()
root.configure(bg="black")
root.configure(bg="black")
root.title('shorts-video-creator')
root.geometry('600x690') #650
root.resizable(False, False)

# Scrollable frame to contain all the widgets
canvas = tk.Canvas(root, bg="#2d2d2d")
frame = tk.LabelFrame(canvas, bg="#2d2d2d")
scrollbar = tk.Scrollbar(root, orient='vertical', command=canvas.yview)
canvas.config(yscrollcommand=scrollbar.set)
scrollbar.pack(side='right', fill='y')
canvas.pack(side='left', fill='both', expand=True)
canvas.create_window((0,0), window=frame, anchor='nw')

# Lists to store image and text-to-speech widgets
image_entries = []
text_entries = []

# Define file path for storing data
DATA_FILE = 'C:\\Users\\enoobis\\Desktop\\video-project\\data\\data.json'

def save_data():
    """Save user input data to a file"""
    data = {}
    for i in range(len(image_entries)):
        image_entry = image_entries[i]
        text_entry = text_entries[i]
        data[f'image_{i+1}'] = {
            'search_term': image_entry.get(),
            'text': text_entry.get('1.0', 'end-1c')
        }
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f)

def load_data():
    """Load user input data from a file"""
    if not os.path.exists(DATA_FILE):
        return
    with open(DATA_FILE, 'r') as f:
        data = json.load(f)
    for i in range(len(image_entries)):
        image_entry = image_entries[i]
        text_entry = text_entries[i]
        key = f'image_{i+1}'
        if key in data:
            image_entry.insert(0, data[key]['search_term'])
            text_entry.insert('1.0', data[key]['text'])


# Five sets of label, entry box, and button for image and text-to-speech
for i in range(5):
    # Label and entry box for image search term
    image_label =customtkinter.CTkLabel(frame, text=f'Image {i+1}:')
    image_label.pack()
    image_entry = customtkinter.CTkEntry(frame)
    image_entry.pack()
    image_entries.append(image_entry)

    # Label and textbox for text-to-speech
    text_label = customtkinter.CTkLabel(frame, text=f'Text for Image {i+1}:')
    text_label.pack()
    text_entry = customtkinter.CTkTextbox(frame, height=5, width=420)
    text_entry.pack()
    text_entries.append(text_entry)

# Load saved data if available
load_data()

#Basic Settings Label
basic_label =customtkinter.CTkLabel(root, text=f'Toolbar')
basic_label.pack()

# Button to save all images and text-to-speech
save_button = customtkinter.CTkButton(root, text='Save All', command=lambda img=image_entries, txt=text_entries: save_all_images_and_mp3(img, txt))
save_button.pack(pady=5,padx=10)

# Button to Cut Images
cutimg_button = customtkinter.CTkButton(root, text="Cut Images", command=process_images)
cutimg_button.pack(pady=5,padx=10)

# Correct image size
corimg_button = customtkinter.CTkButton(root, text='Correct Images', command=resize_images)
corimg_button.pack(pady=5,padx=10)

# Tt correction 9:16 size 
tt_button = customtkinter.CTkButton(root, text="Add Borders", command=add_borders)
tt_button.pack(pady=5,padx=10)

# Button to Add Text to Images
textimg_button = customtkinter.CTkButton(root, text="Add Text to Images", command=add_text_to_images)
textimg_button.pack(pady=5,padx=10)

# Button to Combine Img&Sound
combsound_button = customtkinter.CTkButton(root, text='Combine Img&Sound', command=combine_images_and_sound)
combsound_button.pack(pady=5,padx=10)

# Button to Combine Videos
combvideo_button = customtkinter.CTkButton(root, text='Combine Videos', command=lambda: combine_videos(r'C:\Users\enoobis\Desktop\video-project\pre-done'))
combvideo_button.pack(pady=5,padx=10)

# Button to Add Music to Video
music_button = customtkinter.CTkButton(root, text="Add Music to Video", command=add_music_to_video)
music_button.pack(pady=5,padx=10)

# Button to delete folder contents
delete_button = customtkinter.CTkButton(root, text='Delete All', command=delete_folders_content)
delete_button.pack(pady=5,padx=10)

# Save and upload buttons
save_button = customtkinter.CTkButton(frame, text='Save', command=save_data)
save_button.pack(pady=5,padx=10)
upload_button = customtkinter.CTkButton(frame, text='Upload', command=load_data)
upload_button.pack(pady=5,padx=10)
test_button = customtkinter.CTkButton(frame, text='Test', command=load_data)
test_button.pack(pady=5,padx=10)


# Progress Label
extra_label =customtkinter.CTkLabel(root, text=f'Progress:')
extra_label.pack(pady=5,padx=10)

label = tk.Label(root)
label.pack(pady=5,padx=10)

# Youtube API
api_label =customtkinter.CTkLabel(root, text=f'Youtube API:')
api_label.pack(pady=5,padx=10)

api_entry = customtkinter.CTkEntry(root)
api_entry.pack(pady=5,padx=10)

# Youtube API Button
api_button = customtkinter.CTkButton(root, text="Run")
api_button.pack(pady=5,padx=10)

empt_label = customtkinter.CTkLabel(root, text=f'')
empt_label.pack(pady=5,padx=10)

# Generate button
generate_button = customtkinter.CTkButton(root, text="Generate")
generate_button.pack(pady=5,padx=10)

# Counting button
counting_button = customtkinter.CTkButton(root, text="Counting")
counting_button.pack(pady=5,padx=10)

extra_label =customtkinter.CTkLabel(root, text=f'Copyright by enoobis')
extra_label.pack(pady=5,padx=10)

# Frame fitting and the scrollable area
frame.update_idletasks()
canvas.config(scrollregion=canvas.bbox('all'))

# GUI Run 
root.mainloop()