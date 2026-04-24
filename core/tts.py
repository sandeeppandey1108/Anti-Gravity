
from gtts import gTTS

def generate_voice(script):
    tts = gTTS(script)
    tts.save("voice.mp3")
    return "voice.mp3"
