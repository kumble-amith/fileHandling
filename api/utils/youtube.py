"""Util File for youtube related actions"""
import yt_dlp
from utils import logger


def download(link : list):

    """Actual download of the youtube video"""
    with yt_dlp.YoutubeDL() as ydl:
        ydl.download(link)

    logger.info("Download complete!")

