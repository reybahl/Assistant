from assistant_functions.speak_listen import speak_listen
from intentclassification.intent_classification import IntentClassifier
from assistant_functions.reply import reply
from assistant_functions.weather import weather
from assistant_functions.location import location

class Assistant:

    def __init__(self, name):
        self.name = name
    
    def reply(self, text):
        intent = intentclassifier.predict(text)
        
        replies = {
            "leaving" : reply,
            "greeting" : reply,
            "weather" : weather.main,
            "location" : location.main
            }

        reply_func = replies[intent]

        if callable(reply_func):
            reply_func(text, intent)

    def main(self):
        while True:
            said = speak_listen.listen()
            print(said)
            self.reply(said)

intentclassifier = IntentClassifier()
assistant = Assistant("Assistant")
assistant.main()