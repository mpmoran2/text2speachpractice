from gtts import gTTS
import os

text = open('blog2.txt', 'r').read()
language='en'
blogoutput=gTTS(text=text,lang=language,slow=False)
blogoutput.save('blogoutput.mp3')
os.system('blogoutput.mp3')