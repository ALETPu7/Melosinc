from fastapi import APIRouter
from fastapi.responses import StreamingResponse
from app.models.music_request import MusicRequest
from app.services.musicgen import generate_music

router = APIRouter()

@router.post("/generate-music")
async def generate_music_route(request: MusicRequest):
    audio = await generate_music(request.prompt, request.duration, request.model_type)
    return StreamingResponse(audio, media_type="audio/wav")