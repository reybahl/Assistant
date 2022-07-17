import pvporcupine
import pyaudio
from assistant_functions.speak_listen import speak_listen
from intentclassification.intent_classification import IntentClassifier
from assistant_functions.reply import reply
from assistant_functions.weather import weather
from assistant_functions.location import location
from assistant_functions.open_browser import assistant_browser
from assistant_functions.date_time import date_time
from assistant_functions.repeat import repeat
import struct
import multiprocessing

class Assistant:

    def __init__(self, name):
        self.name = name
        
    
    def reply(self, text):
        intent = intentclassifier.predict(text)
        if intent == 'leaving':
            speak_listen.say("Exiting")
            quit()

        replies = {
            'greeting' : reply,
            'insult' : reply,
            'personal_q' : reply,
            'weather' : weather.main,
            'location' : location.main,
            'open_in_browser':assistant_browser.main,
            'date_time': date_time.main,
            'repeat': repeat.repeat
            }

        try:
            reply_func = replies[intent]

            if callable(reply_func):
                reply_func(text, intent)
        except KeyError:
            speak_listen.say("Sorry, I didn't understand")
        except Exception as e:
            print("Error: " + str(e))

    def main(self):
        print("ready")
        self.porcupine = None
        pa = None
        audio_stream = None


        self.porcupine = pvporcupine.create(keywords=["jarvis"])

        pa = pyaudio.PyAudio()

        audio_stream = pa.open(
                        rate=self.porcupine.sample_rate,
                        channels=1,
                        format=pyaudio.paInt16,
                        input=True,
                        frames_per_buffer=self.porcupine.frame_length)
        
        while True:
            
            try:
                pcm = audio_stream.read(self.porcupine.frame_length)
                pcm = struct.unpack_from("h" * self.porcupine.frame_length, pcm)
            except:
                audio_stream = pa.open(
                        rate=self.porcupine.sample_rate,
                        channels=1,
                        format=pyaudio.paInt16,
                        input=True,
                        frames_per_buffer=self.porcupine.frame_length)

            keyword_index = self.porcupine.process(pcm)

            if keyword_index >= 0:
                print("Hotword Detected")
                
                try: #Tries terminating an action if it exists
                    action.terminate()
                except:
                    pass

                if audio_stream is not None:
                    audio_stream.close()
                said = speak_listen.listen() #Listens for user input
                print(said)

                #action = multiprocessing.Process(target=

                self.reply(said)
                # self.reply(said) Unused
                # action.start()
                # action.join()
                
    

intentclassifier = IntentClassifier()
assistant = Assistant("Assistant")
assistant.main()