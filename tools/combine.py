import os
import click
from moviepy.editor import concatenate_videoclips, VideoFileClip

def calculate_dimensions(clip, target_res):
    clip_aspect_ratio = clip.w / clip.h
    target_aspect_ratio = target_res[0] / target_res[1]

    if clip_aspect_ratio > target_aspect_ratio:
        return (target_res[0], int(target_res[0] / clip_aspect_ratio))
    else:
        return (int(target_res[1] * clip_aspect_ratio), target_res[1])

@click.command()
@click.option('--directory', prompt='Directory', help='The directory containing the files.')
def create_combined_video(directory):
    files = os.listdir(directory)
    clips = []

    # Define a common resolution
    common_resolution = (480, 360)  # Modify as needed

    for file in files:
        path = os.path.join(directory, file)

        # Check if the file is a video (.mp4) or a GIF
        if file.endswith('.mp4') or file.endswith('.gif'):
            clip = VideoFileClip(path)
            new_res = calculate_dimensions(clip, common_resolution)
            clip_resized = clip.resize(new_res)
            clips.append(clip_resized)

    # Create final clip
    final_clip = concatenate_videoclips(clips)

    # Write the result to a file
    final_clip.write_videofile(os.path.join(directory, 'output.mp4'), codec='libx264')

if __name__ == "__main__":
    create_combined_video()
