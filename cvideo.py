from moviepy.editor import *
import os

# Define function to combine images and sound
def combine_images_and_sound():
    # Paths to folders
    image_folder = r'C:\Users\enoobis\Desktop\video-project\text-images'
    audio_folder = r'C:\Users\enoobis\Desktop\video-project\voices'
    output_folder = r'C:\Users\enoobis\Desktop\video-project\pre-done'

    # Get list of image and audio files
    image_files = [f for f in os.listdir(image_folder) if f.endswith('.jpg')]
    audio_files = [f for f in os.listdir(audio_folder) if f.endswith('.mp3')]

    # Combine each image with its corresponding audio file
    for i in range(len(image_files)):
        image_file = os.path.join(image_folder, image_files[i])
        audio_file = os.path.join(audio_folder, audio_files[i])
        output_file = os.path.join(output_folder, f'{i+1}.mp4')

        # Load image and audio into moviepy clips
        image_clip = ImageClip(image_file).set_duration(AudioFileClip(audio_file).duration)
        audio_clip = AudioFileClip(audio_file)

        # Combine image and audio and save as video file
        final_clip = image_clip.set_audio(audio_clip)
        final_clip.write_videofile(output_file, fps=24)