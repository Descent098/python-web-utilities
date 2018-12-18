from pytube import YouTube
import tkinter as tk
from tkinter import filedialog


def link_and_path():
    """Prompts user for the link to a youtube video, and path of where to download the video to"""
    video_url = input("What is the URL for the video you want to download?: ")
    root = tk.Tk()
    root.withdraw()
    file_path = str(filedialog.askdirectory(
        title="Select Video Output directory",
        mustexist=False))
    return video_url, file_path


def download(video_url, path):
    """Takes video URL and output path as input, and downloads a video to the path"""
    YouTube(video_url).streams.first().download(path)
    video_title = str(YouTube(video_url).title)
    return("Downloaded {} to {} as {}.mp4".format(video_title, path, video_title))


def menu_options():
    """Called from main program; compartmentalizing menu options per utility"""
    script_choice = eval(input("\nWhich utility would you like to use? \n(1)Download Video: "))

    # Youtube Downloader
    if script_choice == 1:
        video_url, file_path = link_and_path()
        return str(download(video_url, file_path))


if __name__ == "__main__":
    menu_options()