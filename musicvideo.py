"""
the code adds background music to a video by combining the video's original audio with a music track.
"""

from moviepy.editor import VideoFileClip, AudioFileClip, CompositeAudioClip
import os

def add_music_to_video():

    basePath = os.getcwd()
    video_path = os.path.join(basePath, 'video', 'output.mp4')
    music_path = os.path.join(basePath, 'music', 'music.mp3')
    video_clip = VideoFileClip(video_path)
    music_clip = AudioFileClip(music_path)
    video_audio = video_clip.audio
    voice_audio = video_audio.subclip(0, video_clip.duration)
    music_clip = music_clip.subclip(0, voice_audio.duration)
    music_clip = music_clip.volumex(0.2)
    combined_audio = CompositeAudioClip([voice_audio, music_clip])
    video_clip.audio = combined_audio
    output_path = os.path.join(basePath, 'video-music', 'output_with_music.mp4')
    video_clip.write_videofile(output_path)

