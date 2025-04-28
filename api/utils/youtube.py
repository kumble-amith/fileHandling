import yt_dlp

def download(link : list):

    # url = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'

    with yt_dlp.YoutubeDL({}) as ydl:
        ydl.download(link)

    print("Download complete!")


if __name__ == '__main__':
    url = 'https://www.youtube.com/watch?v=0LD3p4oNuM8'

    download([url])