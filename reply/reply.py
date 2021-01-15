import json
from reply.determine_most_similar import determine_most_similar_phrase
import random

def reply(intent, text):
    with open(f'samples/{intent}.json') as samplesfile:  
        samples = json.load(samplesfile)

    most_similar = determine_most_similar_phrase(text = text, intent_dict = samples)

    if type(samples[most_similar]) == str:
        return samples[most_similar]
    elif type(samples[most_similar]) == list:
        return random.choice(samples[most_similar])