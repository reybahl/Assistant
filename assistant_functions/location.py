import geocoder

class Location:
    def get_lat_lng(self):
        g = geocoder.ip('me')
        return g.latlng[0], g.latlng[1]

    def get_city_state_country(self):
        g = geocoder.ip('me')

        return [g.city, g.state, g.country]
location = Location()
print(location.get_city_state_country())