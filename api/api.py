"""Overall File to handle the all the api related routes"""

from fastapi import FastAPI
from routers.ping import router as ping_router
from routers.youtube import router as yt_router
from routers.split import router as split_router
from utils import logger

app = FastAPI()

app.include_router(router=ping_router, prefix="/ping")
app.include_router(router=yt_router, prefix="/youtube")
app.include_router(router=split_router , prefix="/split_file")
logger.debug("The routers available are %s ", app.routes)
