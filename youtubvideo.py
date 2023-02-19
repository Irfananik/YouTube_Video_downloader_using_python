#how to download youtub video using python!

from pytube import YouTube

link = input("Please enter your video link which you want to download: ")
yt = YouTube(link)

print("Title: ", yt.title)
print("Views: ", yt.views)
print("Seconds: ", yt.length)
ys = yt.streams.get_highest_resolution()

print("Downloading on process please wait.....!")
ys.download()
print("Download completed!")