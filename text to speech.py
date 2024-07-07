from gtts import gTTS
import os

def generate_audio(text):
    tts = gTTS(text=text, lang='en')
    tts.save("output.mp3")
    os.system("afplay output.mp3") 
    os.remove("output.mp3") 


generate_audio("Namashree")
