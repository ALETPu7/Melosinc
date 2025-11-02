from pydantic import BaseModel

class MusicRequest(BaseModel):
    prompt: str
    duration: int
    model_type: str