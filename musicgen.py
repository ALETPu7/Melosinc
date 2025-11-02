from audiocraft.models import MusicGen
import io

async def generate_music(prompt: str, duration: int, model_type: str):
    model = MusicGen.get_pretrained(model_type)
    model.set_generation_params(duration=duration)
    output = model.generate([prompt])
    buffer = io.BytesIO()
    output[0].save(buffer, format="wav")
    buffer.seek(0)
    return buffer