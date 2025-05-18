"""Constants required for overall project for api"""

YDL_OPTIONS = {
    "mp3": {
        "format": "bestaudio/best",
        "ffmpeg_location": "/opt/homebrew/bin/ffmpeg",
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }
        ],
    },
    "mp4": {"format": "mp4"},
}

SPLIT_ALLOWED_FILE_TYPES = ("mp3",)
