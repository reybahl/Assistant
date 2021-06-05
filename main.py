import pvporcupine
import pyaudio
from assistant_functions.speak_listen import speak_listen
from intentclassification.intent_classification import IntentClassifier
from assistant_functions.reply import reply
from assistant_functions.weather import weather
from assistant_functions.location import location
import struct

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
        porcupine = None
        pa = None
        audio_stream = None


        porcupine = pvporcupine.create(keywords=["jarvis"])

        pa = pyaudio.PyAudio()

        audio_stream = pa.open(
                        rate=porcupine.sample_rate,
                        channels=1,
                        format=pyaudio.paInt16,
                        input=True,
                        frames_per_buffer=porcupine.frame_length)
        while True:
            pcm = audio_stream.read(porcupine.frame_length)
            pcm = struct.unpack_from("h" * porcupine.frame_length, pcm)

            keyword_index = porcupine.process(pcm)

            if keyword_index >= 0:
                print("Hotword Detected")
                if audio_stream is not None:
                    audio_stream.close()
                said = speak_listen.listen()
                print(said)
                self.reply(said)
    

intentclassifier = IntentClassifier()
assistant = Assistant("Assistant")
assistant.main()