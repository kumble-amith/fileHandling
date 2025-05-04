import yt_dlp

def download(link : list):


    with yt_dlp.YoutubeDL() as ydl:
        ydl.download(link)

    print("Download complete!")

