from imports import *

def poluchit_transkript(audio_path: str) -> str:
    model = whisper.load_model("small")  # где-то вычитал что small лучше распознает русский
    result = model.transcribe(audio_path, language="ru", fp16=False)
    return result["text"]