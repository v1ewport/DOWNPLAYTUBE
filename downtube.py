import pytube
from moviepy.editor import VideoFileClip
import music_tag
import os

URL = input("URL: ")
PLIST_NAME = input("PLAYLIST NAME: ")

print("DOWNLOADING...")
VIDEO = pytube.YouTube(URL)
STREAM = VIDEO.streams.get_by_itag(18)
STREAM.download()
FILENAME = STREAM.default_filename
print(FILENAME)

print("CONVERTING...")
CLIP = VideoFileClip(FILENAME)
CLIP.audio.write_audiofile(FILENAME[:-4] + ".mp3")
CLIP.close()

print("CLEANING...")
os.system("rm *.mp4")

print("SETTING...")
print(FILENAME[:-4] + ".mp3")
F = music_tag.load_file(FILENAME[:-4] + ".mp3")
F['album'] = PLIST_NAME
F.save()

print("DONE")
