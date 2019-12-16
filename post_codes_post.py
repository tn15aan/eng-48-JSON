import requests
import json

# Making a POST Request

# We need a path
# We need a json object to send
# Possibly headers, depending on the api

# Creating the json
dictionary_post_codes = {
    'postcodes': ['EC2Y 5AS', 'e146gt', 'CT1 2EH'] # Make sure postcodes is written the same as http://postcodes.io/
}

# pass in our dictionary for json
json_body = json.dumps(dictionary_post_codes)

# The url
base_url = 'http://api.postcodes.io/'
path = 'postcodes/'

# The headers
headers = {'Content-type': 'application/json'}


# Making the request
postcodes_post_response = requests.post(base_url+path, data=json_body, headers=headers) # Passing in our data

print(postcodes_post_response.json())

results = postcodes_post_response.json()['result']

# Print the NHS locations in result
for request in results:
    print(request['result']['nhs_ha'])