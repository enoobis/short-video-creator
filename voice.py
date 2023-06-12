import pyttsx3
import os
import tkinter as tk
from tkinter import filedialog

# Initialize the TTS engine
engine = pyttsx3.init()

# Set female voice
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def save_as_mp3(text):
    # Convert the input text to speech
    engine.runAndWait()

    # Save the output as an MP3 file
    directory = "C:/Users/enoobis/Desktop/video-project/voices"
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