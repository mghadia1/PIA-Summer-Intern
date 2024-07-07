import speech_recognition as sr 

r = sr.Recognizer()

def listen(duration=0.1):
    try:
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source, duration=duration)
            audio = r.listen(source)
        return r.recognize_google(audio)
    except sr.RequestError:
        print("Can't get results?")
    except sr.UnknownValueError:
        return ""


if __name__ == "__main__":
    recognized_text = listen(duration=0.5)  
    if recognized_text:
        print("You said:", recognized_text)
    else:
        print("No speech detected or couldn't recognize speech.")