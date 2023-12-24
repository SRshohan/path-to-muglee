import googlemaps
from geopy.distance import distance

import os
import constants


API_KEY = constants.GMAPSAPI

gmaps = googlemaps.Client(key=API_KEY)

location = (40.758896, -73.985130)  # Example: Times Square
radius = 1000  # in meters
place_type = 'restaurant'

places_result = gmaps.places_nearby(location=location, radius=radius, type=place_type)

for place in places_result['results']:
    name = place['name']
    place_location = (place['geometry']['location']['lat'], place['geometry']['location']['lng'])
    place_distance = distance(location, place_location).miles
    vicinity = place.get('vicinity')


    print(f"Name: {name}, Distance: {place_distance:.2f} miles, Vicinity: {vicinity}")