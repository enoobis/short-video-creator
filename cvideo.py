"""The code combines each .jpg image with a corresponding .mp3 audio file from separate folders
and saves it to pre-done folder"""

from moviepy.editor import *
import os

def combine_images_and_sound():
    image_folder = os.path.join(os.getcwd(), "text-images")
    audio_folder = os.path.join(os.getcwd(), "voices")
    output_folder = os.path.join(os.getcwd(), "pre-done")

    image_files = [f for f in os.listdir(image_folder) if f.endswith('.jpg')]
    audio_files = [f for f in os.listdir(audio_folder) if f.endswith('.mp3')]

    for i in range(len(image_files)):
        image_file = os.path.join(image_folder, image_files[i])
        audio_file = os.path.join(audio_folder, audio_files[i])
        output_file = os.path.join(output_folder, f'{i+1}.mp4')

        image_clip = ImageClip(image_file).set_duration(AudioFileClip(audio_file).duration)
        audio_clip = AudioFileClip(audio_file)

        final_clip = image_clip.set_audio(audio_clip)
        final_clip.write_videofile(output_file, fps=24)