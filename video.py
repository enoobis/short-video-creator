import os 
from moviepy.editor import VideoFileClip, concatenate_videoclips, CompositeVideoClip
from moviepy.video.fx import all as afx

# Set the paths
output_folder = os.path.join(os.getcwd(), 'video') # Output folder for the combined video
output_file = 'output.mp4' # Output file name
delay = 2.5  # in seconds
transition_duration = 1.0  # in seconds

# Define a function to execute the task
def combine_videos(input_folder):
    # Get a list of all MP4 files in the input folder
    input_files = [f for f in os.listdir(input_folder) if f.endswith('.mp4')]

    # Create a list of video clips from the input files
    clips = []
    for f in input_files:
        filepath = os.path.join(input_folder, f)
        clip = VideoFileClip(filepath)
        clips.append(clip)

    # Add the delay to each clip
    clips_with_delay = []
    for clip in clips:
        background = CompositeVideoClip([clip], size=clip.size)
        overlay = background.set_position(('center', 'center')).set_start(delay)
        clips_with_delay.append(overlay)

    # Add fade in and out transitions between clips
    transitions = []
    for i in range(len(clips_with_delay) - 1):
        transition = clips_with_delay[i].fadeout(transition_duration/2)\
                                        .fx(afx.fadein, duration=transition_duration/2)
        transitions.append(transition)
    transitions.append(clips_with_delay[-1].fadeout(transition_duration/2))  # Add the last clip with fade out effect

    # Concatenate the clips with transitions into a single clip
    final_clip = concatenate_videoclips(transitions)

    # Save the final clip to the output file
    output_path = os.path.join(output_folder, output_file)
    final_clip.write_videofile(output_path)