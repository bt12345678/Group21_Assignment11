'''
Created on Nov 13, 2022

@author: truax
'''

# https://niaid.github.io/3dpx_api/use_api/

import json  #built in, no pip required (if needed, uses "jsons" import)
import requests

# API KEY = YgtWsNG7O2L9uLaqttPRLgi8J1zgC5l9FkMQdQIB

response = requests.get('http://api.data.gov/nih/3dprint/model/1.0/model_single.json?model_id=000914&api_key=4WHycwdOuvs2FA5TrfmDHGuMid6x5b5ZnRYsqVLG')
json_string = response.content

parsed_json = json.loads(json_string) # Now we have a python dictionary
    
# total = int(parsed_json['total'])        # The number of parks that were returned
    
# for park in parsed_json['data']: 
    # get the value associated with parsed_json['data'] 
#    print (park)

#lets see if this works
print(parsed_json)
#print(parsed_json['data'][0])