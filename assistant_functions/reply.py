import json
from assistant_functions.determine_most_similar import determine_most_similar_phrase
from assistant_functions.speak_listen import speak_listen
import random

def reply(text, intent):
    with open(f'samples/{intent}.json') as samplesfile:  
        samples = json.load(samplesfile)

    most_similar = determine_most_similar_phrase(text = text, intent_dict = samples)

    if type(samples[most_similar]) == str:
        speak_listen.say(samples[most_similar])
    elif type(samples[most_similar]) == list:
        speak_listen.say(random.choice(samples[most_similar]))