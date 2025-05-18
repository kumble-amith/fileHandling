import typing

from fastapi import APIRouter
from fastapi.responses import JSONResponse
from utils.constants import SPLIT_ALLOWED_FILE_TYPES
from utils.split_file.mp3 import split_audio
from utils.utils import get_file_type, is_file_exists

router = APIRouter()

@router.post("/" , status_code=200)
def split_file(params : dict[str , typing.Any]):
    # TODO  modify code to have a single return statement 
    source_file = params['source']
    if is_file_exists(source_file):
        file_type = get_file_type(source_file)
        if file_type in SPLIT_ALLOWED_FILE_TYPES:
            match file_type:
                case mp3:
                    resp = split_audio(params)
        else:
            return JSONResponse(status_code=400 , content=f"The provided file type is not supported.\nPlease select from {SPLIT_ALLOWED_FILE_TYPES} ")
    else:
        return JSONResponse(status_code=400 , content="Invalid File Path, Provide proper file path")