import os
import pytube 
from tqdm import tqdm

def downloader():
    # Ask the user to enter the URL of the YouTube video
    video_url = input("Enter the URL here: ")

    # Create an instance of the YouTube video
    video_instance = pytube.YouTube(video_url)
    stream = video_instance.streams.get_highest_resolution()

    # Ask the user for the folder to save the file
    download_folder = input("Enter the folder to save the file (press Enter for current directory): ").strip()
    if not download_folder:
        download_folder = os.getcwd()

    # Get the video title
    video_title = video_instance.title

    # Define the progress bar
    progress_bar = tqdm(total=stream.filesize, unit="B", unit_scale=True, unit_divisor=1024)

    def progress_callback(stream, chunk, bytes_remaining):

        progress_bar.update(len(chunk))

    # Download the video with progress
    video_instance.register_on_progress_callback(progress_callback)
    stream.download(output_path=download_folder, filename=video_title)

    # Close the progress bar
    progress_bar.close()

if __name__ == '__main__':
    downloader()
