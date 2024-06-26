from pytube import Playlist
import os
from moviepy.editor import *

##Customize these##
playlistLink = "https://www.youtube.com/playlist?list=PL9jb2gW-iFAACVtpNGzMmFHxEWM9UvdoI"
downloadPath = "D:\.My folder\Personal stuff\coding stuff\Coding Projects\Music from YouTube\Music"

#removes illegal characters from title
def NameFix(name):
    fixedVideoTitle = ""
    for i in range(len(name)):
            if name[i] != "," and name[i] != "." and name[i] != "'" and name[i] != "/":
                fixedVideoTitle += name[i]
    return fixedVideoTitle

#removes any remaining mp4s
def CleanupMp4(rawDirectory):
    Dir = (os.listdir(rawDirectory))
    print("checking for any remaining .mp4s")
    for file in Dir:
        if file[-1] == "4":
            os.remove(f"{rawDirectory}\{file}")
    print("cleaned")
    

##Main##
p = Playlist(playlistLink)
print(f"Downloading {p.title}")
Dir = (os.listdir(downloadPath))
fileCounter = 0
DirSize = p.length


for video in p.videos:
    exist = False
    fixedVideoTitle = NameFix(video.title)

    #checks for already installed audio
    for file in Dir:
        if fixedVideoTitle +".mp3" == file:
            exist = True
            fileCounter = fileCounter + 1
            print(f"{fileCounter}/{DirSize} Skipped {file}")

    if exist == False:

        #downloads mp4,mp3 and uninstalls mp4
        video.streams.first().download(downloadPath)
        videoConvert = VideoFileClip(os.path.join(f"{downloadPath}\{fixedVideoTitle}.mp4"),verbose=False)
        videoConvert.audio.write_audiofile(os.path.join(f"{downloadPath}\{fixedVideoTitle}.mp3"),verbose=False, logger=None)
        videoConvert.close()
        os.remove(f"{downloadPath}\{fixedVideoTitle}.mp4")
        fileCounter += 1
        print(f"{fileCounter}/{DirSize} Downloaded {video.title}")
        
print(f"Downloaded {p.title}")
CleanupMp4(downloadPath)



