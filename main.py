'''
Name: Isaac Hedges, Ben Truax
email: hedgesic@mail.uc.edu, truaxbp@mail.uc.edu
Assignment: Assignment 11
Course: IS 4010
Semester/Year: Fall 2022
Brief Description: Pulling from an API and analyzing the data
Citations:
Anything else that's relevant: API Key --> gdowkA6Rae2EbeTngzMUgHSm7Ul1CrFnoEgMQqf5
'''
import json  #built in, no pip required (if needed, uses "jsons" import)
import requests

response = requests.get('https://api.commerce.gov/api/blogs?api_key=gdowkA6Rae2EbeTngzMUgHSm7Ul1CrFnoEgMQqf5')
json_string = response.content
    
parsed_json = json.loads(json_string) # Now we have a python dictionary
    
#print(parsed_json)
#print(parsed_json['data'][0]['description'])
#print(parsed_json['data'][0]['directionsInfo'])
    
total = int(parsed_json['total'])        # The number of parks that were returned
    
for park in parsed_