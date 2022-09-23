import sqlite3
import os
import random
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

conn = sqlite3.connect('userlog.db')
c = conn.cursor()

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

    def logEntry(query, keyword):
        c.execute("INSERT INTO Userlog (Query, Keyword) VALUES (?, ?)", [query, keyword])
        conn.commit()

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

    def jokes():
        lno=random.randint(0,4)
        f=open('jokes.txt', encoding="utf8")
        line=f.readlines()
        txt=line[lno]
        print(txt)
        mal=gTTS(txt,lang='ml')
        mal.save("voice.mp3")
        playsound("voice.mp3")
        os.remove("voice.mp3")
        f.close()


    if 'പേര്' in text:
        myName() 
        logEntry(text, 'പേര്')  

    elif 'എന്തൊക്കെയുണ്ട് വിശേഷം' in text:
        howAreYou()
        logEntry(text, 'എന്തൊക്കെയുണ്ട് വിശേഷം')

    elif 'സമയം' in text:
        currentTime()
        logEntry(text, 'സമയം')
        
    elif 'തീയതി' in text:
        currentDate()
        logEntry(text, 'തീയതി')

    elif 'ആരാണ്' in text:
        whoIs()
        logEntry(text, 'ആരാണ്')

    elif 'കേൾക്കണം' in text:
        song=text.replace('കേൾക്കണം','')
        pywhatkit.playonyt(song)
        logEntry(text, 'കേൾക്കണം')

    elif 'കാണണം' in text:
        film=text.replace('കാണണം','')
        pywhatkit.playonyt(film)
        logEntry(text, 'കാണണം')

    elif 'തമാശ' in text:
        jokes()
        logEntry(text, 'തമാശ')


root = tkinter.Tk()
root.title('ശ്രുതി')
canvas = tkinter.Canvas(root, width=700, height=550)
canvas.pack()
tk_img = ImageTk.PhotoImage(file = "splash.png")
canvas.create_image(350, 300, image=tk_img) 
photo = PhotoImage(file = r"button.png")
quit_button = tkinter.Button(root, image = photo, command = beginListening, anchor = 'w')
quit_button.pack()
root.mainloop()