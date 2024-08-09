"""the code combines .mp4 videos from an input folder into a single video"""

import os 
from moviepy.editor import VideoFileClip, concatenate_videoclips, CompositeVideoClip
from moviepy.video.fx import all as afx

output_folder = os.path.join(os.getcwd(), 'video')
output_file = 'output.mp4'
delay = 2.5 
transition_duration = 1.0  

def combine_videos(input_folder):
    input_files = [f for f in os.listdir(input_folder) if f.endswith('.mp4')]

    clips = []
    for f in input_files:
        filepath = os.path.join(input_folder, f)
        clip = VideoFileClip(filepath)
        clips.append(clip)

    clips_with_delay = []
    for clip in clips:
        background = CompositeVideoClip([clip], size=clip.size)
        overlay = background.set_position(('center', 'center')).set_start(delay)
        clips_with_delay.append(overlay)

    transitions = []
    for i in range(len(clips_with_delay) - 1):
        transition = clips_with_delay[i].fadeout(transition_duration/2)\
                                        .fx(afx.fadein, duration=transition_duration/2)
        transitions.append(transition)
    transitions.append(clips_with_delay[-1].fadeout(transition_duration/2))

    final_clip = concatenate_videoclips(transitions)

    output_path = os.path.join(output_folder, output_file)
    final_clip.write_videofile(output_path)