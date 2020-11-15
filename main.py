import pyttsx3
import speech_recognition as sr

class Assistant():


    def __init__(self, name):
        self.name = name
        self.speech_engine = pyttsx3.init()

    def say(self, text):
        self.speech_engine.say(text)
        self.speech_engine.runAndWait()

    def listen(self):
        self.r = sr.Recognizer()
        
        self.mic = sr.Microphone(device_index=2)
        with self.mic as source:
            audio = self.r.listen(source)

        return (self.r.recognize_google(audio))

assistant = Assistant("Assistant")
assistant.say(assistant.listen())