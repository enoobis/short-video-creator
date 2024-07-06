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
    directory = os.path.join(os.getcwd(), 'voices') # Output folder for the audio files
    counter = 1 # Counter for naming the audio files
    while True: # Loop until a unique filename is found
        filename = f"{counter}.mp3" # Create audio file name
        filepath = os.path.join(directory, filename) # Create audio file path
        if not os.path.exists(filepath): # Check if the file already exists
            break
        counter += 1 # Increment the counter if the file already exists
    engine.save_to_file(text, filepath) # Save the audio to the file
    engine.runAndWait() # Wait for the audio to be saved
    print(f'Audio Successfully saved as {filename}') # Print success message