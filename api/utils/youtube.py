"""Util File for youtube related actions"""

import typing

import requests
import yt_dlp
from utils import logger
from utils.constants import YDL_OPTIONS


def extract_video_info(url: str):
    """Fires a request.get call on the required url for the gathering of additional details """
    embed_url = f"https://www.youtube.com/oembed?url={url}&format=json"
    resp = requests.get(url=embed_url, timeout=20)
    return resp.json()


def download(payload: dict[str, typing.Any]):
    """Actual download of the youtube video"""

    file_format = payload["format"]
    url = payload["link"]
    ydl_opts = YDL_OPTIONS.get(file_format, {})

    logger.info("Selected options are %s ", ydl_opts)

    info = None
    try:

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
            info = extract_video_info(url)

    except Exception as ge:
        logger.error("An Unexpected Error Occurred %s " , ge)
        return str(ge) , False
    
    logger.debug("Video Details %s ", info)
    logger.info("Downloaded Successfully !!! %s ", info.get("title"))
    logger.info("Download complete!")
    return "Download Success" , True