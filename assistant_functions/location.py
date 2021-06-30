from assistant_functions.determine_most_similar import determine_most_similar_phrase
import geocoder
from assistant_functions.speak_listen import speak_listen
class Location:

    def main(self, text, intent):
        samples = {
            "where are we" : {'function' : self.say_location, 'type' : 'location'},
            "location" : {'function' : self.say_location, 'type' : 'location'},
            "city" : {'function' : self.say_location, 'type' : 'city'},
            "state" : {'function' : self.say_location, 'type' : 'state'},
            "country" : {'function' : self.say_location, 'type' : 'country'}
        }

        most_similar = determine_most_similar_phrase(text, samples)
        function = samples[most_similar]['function']
        function(samples[most_similar]['type'])

    def get_lat_lng(self):
        g = geocoder.ip('me')
        return g.latlng[0], g.latlng[1]

    def get_city_state_country(self):
        g = geocoder.ip('me')

        return [g.city, g.state, g.country]

    def say_location(self, type):
        if type == 'location':
            speak_listen.say(" ".join(self.get_city_state_country()))
        if type == 'city':
            speak_listen.say(self.get_city_state_country()[0])
        if type == 'state':
            speak_listen.say(self.get_city_state_country()[1])
        if type == 'country':
            speak_listen.say(self.get_city_state_country()[2])

location = Location()