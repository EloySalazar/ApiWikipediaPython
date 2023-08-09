from gtts import gTTS
from playsound import playsound

import wikipedia

idiom = ""

print("option 1 spanish")
print("ooption 2 english")
print("write option 1 or 2")

option = input(">>")

if option == "1":
    wikipedia.set_lang("es")
    text = input("Que desea averiguar?: ")
    result = wikipedia.summary(text,sentences = 6)
    print(result)
    tts = gTTS(result, lang='es-us')
    tts.save("sound.mp3")
    playsound("sound.mp3")

else:
    wikipedia.set_lang("en")
    text = input("What do you want to find out?:")
    result = wikipedia.summary(text,sentences = 6)
    print(result)
    tts = gTTS(result, lang='es-us')
    tts.save("sound.mp3")
    playsound("sound.mp3")
