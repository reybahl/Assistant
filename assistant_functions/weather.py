import requests
import json
from assistant_functions.location import Location
from assistant_functions.speak_listen import speak_listen
from assistant_functions.determine_most_similar import determine_most_similar_phrase
import pyowm


class Weather:
    def __init__(self):
        with open('weathertoken.txt', 'r') as weathertoken:
            self.own= pyowm.OWM(weathertoken.read()).weather_manager()

    def main(self, text, intent):
        samples = {
            'what is the weather' : {'function' : self.get_weather_at_current_location, 'type' : 'weather'},
            'temperature' : {'function' : self.get_weather_at_current_location, 'type' : 'temperature'},
            'humidity' : {'function' : self.get_weather_at_current_location, 'type' : 'humidity'},
            'forecast' : {'function' : self.get_weather_forecast, 'type' : 'forecast'}
        }

        most_similar = determine_most_similar_phrase(text, samples)
        func = samples[most_similar]['function']
        speak_listen.say(func(samples[most_similar]['type']))
    
    def get_weather_at_current_location(self, type):
        lat, lng = location.get_lat_lng()
        weather = self.own.weather_at_coords(lat, lng).weather
        city = location.get_city_state_country()[0]
        temperature = int(round(weather.temperature(unit='fahrenheit')['temp'], 0))

        if type == 'temperature':
            return f"Currently, the temperature in {city} is {temperature} degrees"
        elif type == 'humidity':
            return f"Currently, the humidity in {city} is {weather.humidity} percent"
        elif type == 'weather':
            return f"Currently in {city}, it's {temperature} degrees and {weather.detailed_status}"

    def get_weather_forecast(self):
        location = Location()
        lat, lng = location.get_lat_lng()

        r = requests.get(f'https://api.weather.gov/points/{lat},{lng}')
        response = json.loads(r.text)
        r = requests.get(response['properties']['forecast'])
        response = json.loads(r.text)

        return response['properties']['periods']

location = Location()

weather = Weather()