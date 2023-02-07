import pytube
from moviepy.editor import VideoFileClip
import music_tag
import os

PLIST_URL = input("PLAYLIST URL: ")
PLIST_NAME = input("PLAYLIST NAME: ")
PLAYLIST = pytube.Playlist(PLIST_URL)
MP4FILES = []

print("DOWNLOADING...")
for URL in PLAYLIST.video_urls:
    VIDEO = pytube.YouTube(URL)
    STREAM = VIDEO.streams.get_by_itag(18)
    STREAM.download()
    print(STREAM.default_filename)
    MP4FILES.append(STREAM.default_filename)

print("CONVERTING...")
for FILE in MP4FILES:
    CLIP = VideoFileClip(FILE)
    CLIP.audio.write_audiofile(FILE[:-4] + ".mp3")
    CLIP.close()

print("CLEANING...")
os.system("rm *.mp4")

print("SETTING...")
for FILE in MP4FILES:
    print(FILE[:-4] + ".mp3")
    F = music_tag.load_file(FILE[:-4] + ".mp3")
    F['album'] = PLIST_NAME
    F.save()

print("DONE")
