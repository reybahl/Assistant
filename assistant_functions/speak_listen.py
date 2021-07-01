import pyttsx3
import speech_recognition as sr
from playsound import playsound


class Speak_Listen:
    def __init__(self):
        self.speech_engine = pyttsx3.init()
        self.speech_engine.setProperty("rate", 150)

        self.r = sr.Recognizer()
        self.mic = sr.Microphone(device_index=2)

    def say(self, text):
        """Uses pyttsx3 engine text-to-speech to to say 'text' argument"""

        self.speech_engine.say(text)
        self.speech_engine.runAndWait()

    def listen(self):
        """Uses speech_recognition library to listen to get audio input and understand what the user is saying"""
    
        with self.mic as source:
            print("listening")
            self.r.non_speaking_duration = 0.5
            audio = self.r.listen(source, timeout=7, phrase_time_limit=5)

        return (self.r.recognize_google(audio))

speak_listen = Speak_Listen()