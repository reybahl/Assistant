import pyttsx3
import speech_recognition as sr
from intentclassification.intent_classification import IntentClassifier
from reply.reply import reply

class Assistant():

    def __init__(self, name):
        self.name = name
        self.speech_engine = pyttsx3.init()

    def say(self, text):
        """Uses pyttsx3 engine text-to-speech to to say 'text' argument"""

        self.speech_engine.say(text)
        self.speech_engine.runAndWait()

    def listen(self):
        """Uses speech_recognition library to listen to get audio input and understand what the user is saying"""
        
        self.r = sr.Recognizer()
        self.mic = sr.Microphone(device_index=2)

        with self.mic as source:
            self.say("Listening!")
            audio = self.r.listen(source)

        return (self.r.recognize_google(audio))
    
    def reply(self, text):
        intent = intentclassifier.predict(text)
        
        replies = {
            "leaving" : reply,
            "greeting" : reply,

            }

        reply_func = replies[intent]

        if callable(reply_func):
            print(reply_func(intent, text)) 

    # def leave(self, text):
    #     print("Bye bye")

intentclassifier = IntentClassifier()
assistant = Assistant("Assistant")
# assistant.say(assistant.listen())

assistant.reply("i have to go")