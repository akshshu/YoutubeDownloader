from moviepy.editor import *
from pytube import YouTube
import os
import sys
import shutil
link = sys.argv[1]
yt = YouTube(link)
# # Title of video
print("Title: ", yt.title)
# # Number of views of video
print("Number of views: ", yt.views)
# # Length of the video
print("Length of video: ", yt.length, "seconds")
# # Description of video
# # print("Description: ", yt.description)
# # Rating
# # print("Ratings: ", yt.rating)
resol = ""
ext = "mp4"
prog = ""
# print(os.getcwd())

try:
    if(sys.argv[2]):
        resol = sys.argv[2]
    if(resol == "720p"):
        prog = True
    if(sys.argv[3]):
        ext = sys.argv[3]

except Exception:
    pass
vidQuality = yt.streams.filter(res=resol, file_extension=ext, progressive=prog)
if len(vidQuality) == 0:
    print("No video available!!")
    exit(1)
for el in vidQuality:
    print(el)
currentUser = os.getlogin()
downloadFolder = os.path.join("C:\\Users", currentUser)
downloadFolder = os.path.join(downloadFolder, "Downloads")

if(prog != True):
    VideotagNo = input("Enter itag to download video :")
    if(VideotagNo != "22"):
        AudiotagNo = input("Enter audio itag to download audio :")
        try:
            shutil.rmtree("tempaud")
        except Exception:
            pass
        try:
            shutil.rmtree("tempvid")
        except Exception:
            pass
        os.mkdir("tempvid")
        os.mkdir("tempaud")
        print("Download in progress...")
        videostream = yt.streams.get_by_itag(VideotagNo)
        videostream.download("tempvid/")
        audiostream = yt.streams.get_by_itag(AudiotagNo)
        audiostream.download("tempaud/")
        videofilepath = os.getcwd()
        vidDir = os.path.join(videofilepath, "tempvid")
        for filname in os.listdir(vidDir):
            videofilepath = os.path.join(vidDir, filname)
        audiofilepath = os.getcwd()
        audDir = os.path.join(audiofilepath, "tempaud")
        for filname in os.listdir(audDir):
            audiofilepath = os.path.join(audDir, filname)
        print("Download finished!!")
        print("Mergin Files : ")
        clip = VideoFileClip(videofilepath)
        clip = clip.subclip()
        audioclip = AudioFileClip(audiofilepath)
        videoclip = clip.set_audio(audioclip)
        videofilename = videofilepath.split("\\")[-1]
        file = os.path.join(downloadFolder, videofilename)
        videoclip.write_videofile(file)
        shutil.rmtree(vidDir)
        shutil.rmtree(audDir)
else:
    videostream = yt.streams.get_by_itag(22)
    print("Download in progress....")
    videostream.download(downloadFolder)
if(VideotagNo == "22"):
    videostream = yt.streams.get_by_itag(22)
    print("Download in progress....")
    videostream.download(downloadFolder)
