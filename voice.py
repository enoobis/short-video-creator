"""The code uses the pyttsx3 text-to-speech engine to convert text to speech and save it as an MP3 file"""

import pyttsx3
import os
import tkinter as tk
from tkinter import filedialog

engine = pyttsx3.init()

voices = engine.getProperty('voices')
for voice in voices:
    if 'English' in voice.name:
        engine.setProperty('voice', voice.id)
        break

def save_as_mp3(text):
    engine.runAndWait()

    directory = os.path.join(os.getcwd(), 'voices') 
    counter = 1 
    while True: 
        filename = f"{counter}.mp3"
        filepath = os.path.join(directory, filename) 
        if not os.path.exists(filepath): 
            break
        counter += 1 
    engine.save_to_file(text, filepath) 
    engine.runAndWait() 
    print(f'Audio Successfully saved as {filename}')
