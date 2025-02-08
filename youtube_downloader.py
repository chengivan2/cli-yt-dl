import sys
import os
from pytube import YouTube

def download_youtube_video(url, output_path):
    try:
        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()
        print(f"Downloading: {yt.title}...")
        stream.download(output_path)
        print("Download completed!")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python youtube_downloader.py <YouTube URL>")
    else:
        youtube_url = sys.argv[1]
        current_directory = os.getcwd()
        download_youtube_video(youtube_url, current_directory)