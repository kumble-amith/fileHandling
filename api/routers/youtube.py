"""Youtube related server activities and routes"""

import typing

from fastapi import APIRouter
from fastapi.responses import JSONResponse
from utils.youtube import download

router = APIRouter()


@router.post("/download", status_code=200)
def yt_download(params: dict[str, typing.Any]):
    """Download the video from youtube"""
    # If in case you are getting a cookies error please try after some time.

    download_info, status = download(params)

    return JSONResponse(status_code=200 if status else 400, content=download_info)
