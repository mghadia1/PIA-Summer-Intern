import os 
import pickle


import mediapipe as mp
import cv2
import matplotlib.pyplot as plt
'''import speech_recognition as sr '''


mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles

hands = mp_hands.Hands(static_image_mode=True, min_detection_confidence=0.3)



DATA_DIR = './data'

data= [] 
labels = [] 

for dir_ in os.listdir(DATA_DIR):
    for img_path in os.listdir(os.path.join(DATA_DIR,dir_))[:1] : 
        data_aux = [] 

        x_ = []
        y_ = []

        img = cv2.imread(os.path.join(DATA_DIR, dir_, img_path))
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


        results = hands.process(img_rgb)
        if results.mutli_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                for i in range(len(mp_hands.landmark)):
                    x = hand_landmarks.landmark[i].x
                    y = hand_landmarks.landmark[i].y
                    data_aux.append(x)
                    data_aux.append(y)

            for i in range(len(hand_landmarks.landmark)):
                    x = hand_landmarks.landmark[i].x
                    y = hand_landmarks.landmark[i].y
                    data_aux.append(x - min(x_))
                    data_aux.append(y - min(y_))


            data.append(data_aux)
            labels.append(dir_)

f= open('data.pickle','wb')
pickle.dump({'data':data , 'labels':labels}, f)

f.close 


'''r = sr.Recognizer()

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
        print("No speech detected or couldn't recognize speech.")'''