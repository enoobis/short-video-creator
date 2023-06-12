from moviepy.editor import VideoFileClip, AudioFileClip, CompositeAudioClip


def add_music_to_video():
    
    
    # Define the paths to the video and music files
    video_path = 'C:/Users/enoobis/Desktop/video-project/video/output.mp4'
    music_path = 'C:/Users/enoobis/Desktop/video-project/music/music.mp3'
    
    # Load the video and music files
    video_clip = VideoFileClip(video_path)
    music_clip = AudioFileClip(music_path)
    
    # Get the audio track from the video clip
    video_audio = video_clip.audio
    
    # Set the duration of the music clip to match the duration of the voice audio in the video clip
    voice_audio = video_audio.subclip(0, video_clip.duration)
    music_clip = music_clip.subclip(0, voice_audio.duration)
    
    # Lower the volume of the music clip by 90%
    music_clip = music_clip.volumex(0.9)
    
    # Combine the voice audio from the video clip with the modified music clip
    combined_audio = CompositeAudioClip([voice_audio, music_clip])
    
    # Set the audio track of the video clip to the combined audio
    video_clip.audio = combined_audio
    
    # Write the final video file with the modified audio
    output_path = 'C:/Users/enoobis/Desktop/video-project/video-music/output_with_music.mp4'
    video_clip.write_videofile(output_path)


