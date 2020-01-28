import pyttsx3
import speech_recognition as sr
from googletrans import Translator

def speaker(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    engine.stop()

def translate(text,language):
    return Translator().translate(text, dest=language).text

def listening():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something...")
        audio = r.listen(source)
    print('Finish listening...')

    speech = ""
    # recognize speech using Google Speech Recognition
    try:
        speech = r.recognize_google(audio)
    except sr.UnknownValueError:
        print("Not understand audio")
    except sr.RequestError:
        print("Could not results")
    finally:
        return str(speech.lower())

while True:
    speech_text = listening()
    print('Recognizable speech: '+speech_text)
    trans_text = translate(speech_text,'ru')
    print('Translated text: ' + trans_text)
    speaker(trans_text)