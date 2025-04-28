from utils import youtube

from fastapi import FastAPI 
from fastapi.responses import JSONResponse
import typing


app = FastAPI()

@app.get("/")
def root():
    return {"home" : "page"}

@app.post("/youtube/download" , status_code=200)
def yt_download(params : dict[str , typing.Any]):
    print(params)
    
    youtube.download(params['link'])

    return JSONResponse(status_code=200 , content="Download Success ")