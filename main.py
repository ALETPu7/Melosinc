from fastapi import FastAPI
from app.routes.music import router as music_router

app = FastAPI()
app.include_router(music_router, prefix="/api")