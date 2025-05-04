"""Ping Server Routes"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse

router = APIRouter()

@router.get("/" , status_code=200)
def ping_server():
    """Function to ping the server to check if the server is LIVE or not"""
    return JSONResponse(status_code=200 , content="Server is LIVE")
