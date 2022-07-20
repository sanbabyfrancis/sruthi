import os
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
import datetime
import wikipedia
import pywhatkit

import tkinter
from tkinter import PhotoImage
from tkinter.ttk import *
from PIL import ImageTk

def beginListening():
    earings=sr.Recognizer()
    try:
        with sr.Microphone() as source:
            playsound("initiate.mp3")
            print("ശ്രുതിയോടു സംസാരിക്കൂ")
            earings.adjust_for_ambient_noise(source)
            voice=earings.listen(source)
            text=earings.recognize_google(voice,language="ml-IN")
            print(text)

    except:
        pass


    def myName():
        txt='എന്റെ പേര് ശ്രുതി'
        mal=gTTS(txt,lang='ml')
        mal.save("voice.mp3")
        playsound("voice.mp3")
        os.remove("voice.mp3")

    def howAreYou():
        txt="എനിക്ക് സുഖമാണ്"
        mal=gTTS(txt,lang='ml')
        mal.save('voice.mp3')
        playsound('voice.mp3')
        os.remove("voice.mp3")

    def currentTime():
        txt=datetime.datetime.now().strftime("%I:%M %p")
        print(txt)
        mal=gTTS(txt,lang='ml')
        mal.save("voice.mp3")
        playsound("voice.mp3")
        os.remove("voice.mp3")

    def currentDate():
        txt=datetime.datetime.now().strftime("%d/%B/%Y")
        print(txt)
        mal=gTTS(txt,lang='ml')
        mal.save("voice.mp3")
        playsound("voice.mp3")
        os.remove("voice.mp3")

    def whoIs():
        person=text.replace('ആരാണ്','')
        wikipedia.set_lang('ml')
        txt=wikipedia.summary(person,3)
        print(txt)
        mal=gTTS(txt,lang='ml')
        mal.save("voice.mp3")
        playsound("voice.mp3")
        os.remove("voice.mp3")


    if 'പേര്' in text:
        myName()    
    elif 'എന്തൊക്കെയുണ്ട് വിശേഷം' in text:
        howAreYou()
    elif 'സമയം' in text:
        currentTime()
    elif 'തീയതി' in text:
        currentDate()
    elif 'ആരാണ്' in text:
        whoIs()
    elif 'കേൾക്കണം' in text:
        song=text.replace('കേൾക്കണം','')
        pywhatkit.playonyt(song)
    elif 'കാണണം' in text:
        film=text.replace('കാണണം','')
        pywhatkit.playonyt(film)


root = tkinter.Tk()
root.title('ശ്രുതി')
canvas = tkinter.Canvas(root, width=700, height=550) # window size
canvas.pack()
tk_img = ImageTk.PhotoImage(file = "splash.png")
canvas.create_image(350, 300, image=tk_img) 
photo = PhotoImage(file = r"button.png")
quit_button = tkinter.Button(root, image = photo, command = beginListening, anchor = 'w')
quit_button.pack()
root.mainloop()