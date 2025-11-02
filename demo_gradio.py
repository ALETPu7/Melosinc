import gradio as gr
from app.services.musicgen import generate_music

def generate(prompt, duration, model_type):
    audio = generate_music(prompt, duration, model_type)
    return audio

gr.Interface(
    fn=generate,
    inputs=[
        gr.Textbox(label="Descripción"),
        gr.Slider(5, 30, label="Duración (segundos)"),
        gr.Dropdown(["facebook/musicgen-small", "facebook/musicgen-medium", "facebook/musicgen-melody"], label="Modelo")
    ],
    outputs=gr.Audio(label="Resultado")
).launch()