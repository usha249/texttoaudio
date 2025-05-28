from gtts import gTTS
import os

text = "please like share and subscribe."
tts = gTTS(text=text, lang='en')
tts.save("op.mp3")

# Play the audio
os.system("start op.mp3")  # For Windows
# os.system("mpg321 output.mp3")  # For Linux/Mac