from gtts import gTTS
import os
from tkinter import *

def text2speach():
    text = entry.get()
    language='en'
    output = gTTS(text=text,lang=language,slow=False)
    output.save('anoutput.mp3')
    os.system('anoutput.mp3')

root = Tk()
canvas = Canvas(root, width=400, height=400)
canvas.pack()

label = Label(text="Enter Text To Convert To Audio")
canvas.create_window(200,130,window=label)

entry = Entry(root)
canvas.create_window(200,180,window=entry)

button = Button(text="Start", command=text2speach)
canvas.create_window(200,230,window=button)

root.mainloop()







# converting a file to audio
# text = open('demo.txt', 'r').read()
# language='en' #can find other language codes by searching google text to speach language codes
# fileoutput=gTTS(text=text,lang=language,slow=False)
# fileoutput.save('fileoutput.mp3')
# os.system('fileoutput.mp3')


#SIMPLE TEXT TO SPEACH
# text = "Oooo sheepy"
# output = gTTS(text=text,lang='en',slow=False)
# output.save('output.mp3')

# os.system('output.mp3')
# # need to run in actual commandline not terminal

