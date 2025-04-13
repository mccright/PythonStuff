from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
import os
import sys
import datetime
import configparser
import json
import requests

# This is an unsafe experiment with flask-restful
# intended for a local, isolated learning environment.
# It can fetch current weather data from OpenWeatherMap
# I started with the example code from:  
# https://github.com/flask-restful/flask-restful/blob/master/examples/todo.py
# and 
# https://flask-restful.readthedocs.io/en/latest/quickstart.html#full-example

app = Flask(__name__)
api = Api(app)

#   "desmoines,us":{"lon":-122.3243,"lat":47.4018}
#   "urbandale,us":{"lon":-93.7122,"lat":41.6267}
#      "denver,us":{"lon":-104.9847,"lat":39.7392}
#      "pueblo,us":{"lon":-104.6091,"lat":38.2545}
#  "middlebury,us":{"lon":-73.1673,"lat":44.0153}
# "bella vista,us":{"lon":-94.2316,"lat":36.4295}
#     "lincoln,us":{"lon":-96.667,"lat":40.8}
#"philadelphia,us":{"lon":-75.1638,"lat":39.9523}
#   "amsterdam,nl":{"lon":4.8897,"lat":52.374}
#        "kofu,jp":{"lon":138.5683,"lat":35.6639}
LOCATIONS = {
    'urbandale': {'city': 'urbandale'},
    'desmoines': {'city': 'desmoines'},
    'westdesmoines': {'city': 'desmoines'},
    'denver': {'city': 'denver'},
    'pueblowest': {'city': 'pueblo'},
    'pueblo': {'city': 'pueblo'},
    'middlebury': {'city': 'middlebury'},
    'bellavista': {'city': 'bella vista'},
    'lincoln': {'city': 'lincoln'},
    'philadelphia': {'city': 'philadelphia'},
}

def abort_if_location_doesnt_exist(location_id):
    if location_id not in LOCATIONS:
        abort(404, message="CityName {} doesn't exist".format(location_id))

parser = reqparse.RequestParser()
parser.add_argument('city')


# Get value from a config file: https://github.com/mccright/PythonStuff/blob/main/otherNotes.md#get-values-from-a-config-file
def get_config(filename, section, val):
    config = configparser.ConfigParser()
    config.read([filename])
    # create an object for a specific config file section
    weather = config[section]
    # now get the values from that object
    return weather.get(val)


# Thank you Matt Arderne at https://gist.github.com/RobertSudwarts/acf8df23a16afdb5837f?permalink_comment_id=3769668#gistcomment-3769668 
# for the calculate_bearing(d) function  
def calculate_bearing(d):
    dirs = ['N', 'NNE', 'NE', 'ENE', 'E', 'ESE', 'SE', 'SSE', 'S', 'SSW', 'SW', 'WSW', 'W', 'WNW', 'NW', 'NNW']
    ix = int(round(d / (360. / len(dirs))))
    return dirs[ix % len(dirs)]


# CityName
#   show a single location item and in the future will let you delete it
class CityName(Resource):
    def get(self, location_id):
        abort_if_location_doesnt_exist(location_id)
        # Start the weather code
        try:
            # Get your OpenWeatherMap token from your config file.
            # This is just experimental code for use at home.  It would not 
            # be risk-appropriate for Internet access.  At a minimum, it would 
            # need some sort of "governor" to resist excess traffic abuse.
            # That MIGHT be a caching mechanism, where calls to a given city 
            # would be cached and "re-used" for 10-minutes or so before making 
            # another API call to OpenWeatherMap.
            owmtoken = get_config('weather.ini', 'weather', 'owmtokenA')
            cityname = LOCATIONS[location_id]['city']
            # Assuming the USA for now. Easy change for international
            cityname = cityname + str(",us")
            url = (f"https://api.openweathermap.org/data/2.5/weather?appid={owmtoken}&lang=en&units=imperial&q={cityname}")
            response = requests.get(url)
            jsonstr = json.loads(response.text)
            posixdt = datetime.datetime.fromtimestamp(int(jsonstr['dt']))
            reporttime = datetime.date.strftime(posixdt, "%Y-%m-%M %R")
            winddir = calculate_bearing(jsonstr['wind']['deg'])
            weatherstr = (f"{reporttime}, {jsonstr['main']['temp']}°F, feels like {jsonstr['main']['feels_like']}°F, wind {winddir} {jsonstr['wind']['speed']} m/h, {jsonstr['weather'][0]['description']}, humidity {jsonstr['main']['humidity']}%")
            return weatherstr, 201

        except Exception as e:
            print("Failed this run. Error: {} -- {}".format(e, (sys.exc_info())))


    # Not implemented safely yet
    def delete(self, location_id):
        abort_if_location_doesnt_exist(location_id)
        del LOCATIONS[location_id]
        return '', 204


    # Not implemented safely yet
    def put(self, location_id):
        args = parser.parse_args()
        city = {'city': args['city']}
        LOCATIONS[location_id] = city
        return city, 201


# ListOfCities
#   shows a list of all cities, and no safe POST option yet
class ListOfCities(Resource):
    def get(self):
        return LOCATIONS


    # Not implemented safely yet
    def post(self):
        args = parser.parse_args()
        city = {'city': args['city']}
        LOCATIONS[location_id] = city
        return LOCATIONS[location_id], 201

##
## Setup the Api resource routing here
##
api.add_resource(ListOfCities, '/cities')
api.add_resource(CityName, '/cities/<string:location_id>')


if __name__ == '__main__':
    app.run(debug=True)
