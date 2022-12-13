from pytube import YouTube
import os
import pywhatkit
import requests
from moviepy.editor import *

directory = "Songs"
os.mkdir(directory)

file_object = open("text.txt", "r+")
l = file_object.readlines()

for x in l:
    y = pywhatkit.playonyt(x, open_video=False)
    url = requests.get(y).url
    yt = YouTube(url)

    video = yt.streams.filter().first()
    destination = directory
    out_file = video.download(output_path=destination)
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp4'
    os.rename(out_file, new_file)

    mp4_file = new_file
    mp3_file = base + '.mp3'
    videoClip = VideoFileClip(mp4_file)
    audioclip = videoClip.audio
    audioclip.write_audiofile(mp3_file)
    audioclip.close()
    videoClip.close()
    os.remove(new_file)


    print(yt.title + " has been successfully downloaded.")


    
