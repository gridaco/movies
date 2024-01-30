import click
from moviepy.editor import VideoFileClip
import os


@click.command()
@click.argument('input_file', type=click.Path(exists=True))
def resize_video(input_file):
    # Extract the file name and extension
    file_name, file_ext = os.path.splitext(input_file)

    # Load the video
    clip = VideoFileClip(input_file)

    # Resize the video
    resized_clip = clip.resize(0.5)  # 50% of the original size

    # Construct the output file name
    output_file = f"{file_name}.0.5x{file_ext}"

    # Determine the codec based on the file extension
    # You can adjust this based on your needs
    codec = 'libx264' if file_ext == '.mp4' else 'prores'

    # Export the resized video
    resized_clip.write_videofile(output_file, codec=codec)
    print(f"Resized video saved as {output_file}")


if __name__ == '__main__':
    resize_video()
