from assistant_functions.location import Location
from assistant_functions.speak_listen import speak_listen
from assistant_functions.determine_most_similar import determine_most_similar_phrase
from datetime import datetime
import random

class DateTime:
    def main(self, text, intent):
        samples = {
            'time' : {'func' : self.time, 'param':None},
            'date' : {'func' : self.date, 'param':None},
            'date year' : {'func' : self.date, 'param':(True)}
        }

        most_similar = determine_most_similar_phrase(text, samples)
        func = samples[most_similar]['func']
        params = samples[most_similar]['param']
        speak_listen.say(func(params))

    def time (self):
        now = datetime.now()
        beginning_strings = ["The time is currently", "It's currently"]
        minute = now.strftime("%M")
        if minute[0] == '0':
            if minute[1] == '0':
                minute = 'o clock'
            else:
                minute = 'o' + minute[1:]

        hour = now.strftime('%I')
        if hour[0] == '0':
            hour = hour[1]

        current_time = f"{hour} {minute} {now.strftime('%p')}" 
        return random.choice(beginning_strings) + " " + current_time
    
    def date(self, year=False):
        now = datetime.now()
        beginning_strings = ["Today is", "It's"]
        month = now.strftime("%B")
        day = now.day
        year_int = now.year
        year_str = str(year_int)[:2] + random.choice(["", " "]) + str(year_int)[2:]
        current_date = f"{month} {day} {year_str if year else ''}" 
        return random.choice(beginning_strings) + " " + current_date

date_time = DateTime()