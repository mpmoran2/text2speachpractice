from gtts import gTTS
import os

text = "Oooo sheepy"
output = gTTS(text=text,lang='en',slow=False)
output.save('output.mp3')

os.system('output.mp3')
# need to run in actual commandline not terminal

