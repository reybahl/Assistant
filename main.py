import pyttsx3

class Assistant():

    
    def __init__(self, name):
        self.name = name
        self.speech_engine = pyttsx3.init()

    def say(self, text):
        self.speech_engine.say(text)
        self.speech_engine.runAndWait()

assistant = Assistant("Assistant")
assistant.say("Hello, how are you?")