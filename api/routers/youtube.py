import typing

from fastapi import APIRouter
from fastapi.responses import JSONResponse
from utils.youtube import download

router = APIRouter()


@router.post("/download", status_code=200)
def yt_download(params: dict[str, typing.Any]):
    print(params)

    download(params["link"])

    return JSONResponse(status_code=200, content="Download Success ")
