"""
Name: Isaac Hedges, Ben Truax 
email: hedgesic@mail.uc.edu, truaxbp@mail.uc.edu
Assignment: Assignment11
Course: IS 4010
Semester/Year: Fall 2022
Brief Description: Writing using an API to find unique information
Citations:
Anything else that's relevant: 
"""

import json  #built in, no pip required (if needed, uses "jsons" import)
import requests

# API URL = https://api.wheretheiss.at/v1/satellites/25544
# API KEY = Open Source
# This API gives information about the current status of the International Space Station

# URL with data request and submit to the server
response = requests.get('https://api.wheretheiss.at/v1/satellites/25544')
json_string = response.content

# Parse the results
parsed_json = json.loads(json_string) # Now we have a python dictionary

# Check on parsed results
print(parsed_json)

# Extracting Interesting Data about current location of ISS
print("Name:", parsed_json['name'])    
print("Latitude:", parsed_json['latitude'])
print("longitude:", parsed_json['longitude'])