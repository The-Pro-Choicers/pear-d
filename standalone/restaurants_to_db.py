import os
import json
from pathlib import Path
import pymysql.cursors

JSONdata = []

with open(os.path.join(Path(__file__).resolve().parent, "restaurants.json")) as f:
    JSONreader = json.load(f)
    JSONdata = dict(JSONreader)

'''
CHANGELOG FOR restaurants.json
- replace "\/" with "/"
- add social good categories
- add food category
- change social good status of certain restaurants, THOUGH THEY ARE STILL INHERENTLY RANDOM AND NOT REPRESENTATIVE OF REAL STATUS OF RESTAURANTS.
'''

connection = pymysql.connect(
    host = 'peard-database.cbiya7huefjt.us-east-1.rds.amazonaws.com',
    user = 'pearddev',
    password = 'Peepeep00p0031!',
    database = 'peard',
    cursorclass = pymysql.cursors.DictCursor
)

with connection:
    with connection.cursor() as cursor:
        # Create a new record
        # https://stackoverflow.com/questions/5785154/python-mysqldb-issues-typeerror-d-format-a-number-is-required-not-str
        sql = "INSERT INTO api_restaurant (name, address, photo_ref, price_level, rating, url, env_conscious, minority, philanthropic, category) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        
        for restaurant in JSONdata['data']:
            
            cursor.execute(
                            sql, (
                                    restaurant['name'],
                                    restaurant['vicinity'],
                                    restaurant['photos'][0]['photo_reference'],
                                    restaurant['price_level'],
                                    restaurant['rating'],
                                    ('https://www.google.com/maps/place/?q=place_id:' + restaurant['place_id']),
                                    restaurant['env_status'],
                                    restaurant['min_status'],
                                    restaurant['phil_status'],
                                    restaurant['food_category']
                                )
                            )
        
        connection.commit()