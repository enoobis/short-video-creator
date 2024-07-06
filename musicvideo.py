from moviepy.editor import VideoFileClip, AudioFileClip, CompositeAudioClip
import os

def add_music_to_video():
    """
    Adds background music to a video by combining the video's original audio with a music track.
    The volume of the music track is lowered to avoid overpowering the original audio.

    This function assumes that the video file is named 'output.mp4' and located in a 'video' folder,
    and the music file is named 'music.mp3' and located in a 'music' folder. The final video with
    combined audio is saved in a 'video-music' folder.
    """
    
    # Get the current working directory
    basePath = os.getcwd()
    
    # Define the paths to the video and music files
    video_path = os.path.join(basePath, 'video', 'output.mp4')
    music_path = os.path.join(basePath, 'music', 'music.mp3')
    
    # Load the video and music files
    video_clip = VideoFileClip(video_path)
    music_clip = AudioFileClip(music_path)
    
    # Get the original audio track from the video clip
    video_audio = video_clip.audio
    
    # Set the duration of the music clip to match the duration of the voice audio in the video clip
    voice_audio = video_audio.subclip(0, video_clip.duration)
    music_clip = music_clip.subclip(0, voice_audio.duration)
    
    # Lower the volume of the music clip by 90%
    music_clip = music_clip.volumex(0.1)
    
    # Combine the voice audio from the video clip with the modified music clip
    combined_audio = CompositeAudioClip([voice_audio, music_clip])
    
    # Set the audio track of the video clip to the combined audio
    video_clip.audio = combined_audio
    
    # Define the output path for the final video file with the modified audio
    output_path = os.path.join(basePath, 'video-music', 'output_with_music.mp4')
    
    # Write the final video file with the modified audio
    video_clip.write_videofile(output_path)

