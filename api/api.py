from utils import youtube

from fastapi import FastAPI 
from fastapi.responses import JSONResponse
import typing


app = FastAPI()

@app.get("/ping" , status_code=200)
def root():
    return JSONResponse(status_code=200 , content= "App is ready to use")

@app.post("/youtube/download" , status_code=200)
def yt_download(params : dict[str , typing.Any]):
    print(params)
    
    youtube.download(params['link'])

    return JSONResponse(status_code=200 , content="Download Success ")