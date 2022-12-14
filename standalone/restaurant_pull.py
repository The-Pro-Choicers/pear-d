# pip install googlemaps
# pip install PyMySQL
# pip install pandas

# REFERENCES:
'''
https://www.youtube.com/watch?v=YwIu2Rd0VKM
https://www.youtube.com/watch?v=qkSmuquMueA
'''

import googlemaps
import time
import os
import pandas as pd
from pathlib import Path

def miles_to_meters(miles):
    try:
        return miles * 1609.344
    except BaseException:
        return 0

# define our API key
# there needs to be a way to make this private - otherwise it is exposed.
API_KEY = ''

with open(os.path.join(Path(__file__).resolve().parent.parent, "credentials", "apikey.txt")) as f:
    API_KEY = f.readline()

# define our client
    # authenticate using the API key.
gmaps = googlemaps.Client(key = API_KEY)

# define a list of restaurants
restaurantList = []

# define our search

    # define our location (the x and y coordinates of UF) as a tuple
    # reference: https://www.google.com/maps/place/University+of+Florida/@29.6436371,-82.3571189,17z/data=!4m14!1m7!3m6!1s0x88e8a30cfbe49275:0x206fe0de143d9886!2sUniversity+of+Florida!8m2!3d29.6436325!4d-82.3549302!16s%2Fm%2F0j_sncb!3m5!1s0x88e8a30cfbe49275:0x206fe0de143d9886!8m2!3d29.6436325!4d-82.3549302!16s%2Fm%2F0j_sncb
UF_coordinates = (29.6436371, -82.3571189)

    # we will be searching within a 5-mile radius, but the search accepts a radius in METERS.
search_radius = miles_to_meters(5)

    # call the search
places_result = gmaps.places_nearby(
    location = UF_coordinates, 
    radius = search_radius,
    type = ['restaurant', 'food']
)

# fill the restaurant list with the results of this API call
restaurantList.extend(places_result.get('results'))

# however, there is a small problem: each search only finds 20 items
    # in order to find the next 20 items, you must call the search again
    # with the next page token.
next_page_token = places_result.get('next_page_token')

while next_page_token:
    time.sleep(2) # there is a pause while the next page is generated by the API.
    places_result = gmaps.places_nearby(
        location = UF_coordinates, 
        radius = search_radius,
        type = ['restaurant', 'food'],
        page_token = next_page_token
    )
    restaurantList.extend(places_result.get('results'))
    next_page_token = places_result.get('next_page_token')

# now, the restaurant list is populated with ALL RESTAURANTS in a 5-mile radius of UF.

'''
Previously deprecated and now reinstated, we are going to export the data from the Google API pull request into a .json file which will be
manually edited to reflect food and social good categories.
'''

# create a data frame using pandas containing each restaurant and its information.
dataframe = pd.DataFrame(restaurantList)
dataframe['url'] = 'https://www.google.com/maps/place/?q=place_id:' + dataframe['place_id']
# export the data frame into a .json file for manual review.
# reference: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_json.html
dataframe.to_json(os.path.join(Path(__file__).resolve().parent, "restaurants.json"), orient='table')

# piping of restaurant objects to database will now be done in a separate file, restaurants_to_db.py.