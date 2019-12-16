import requests
import json



# Make sure postcodes is written the same as http://postcodes.io/



# The url
base_url = 'http://api.postcodes.io/'
path = 'postcodes/'

# The headers
headers = {'Content-type': 'application/json'}

def inputted_postcodes():
    postcode1 = input('Enter the postcode: ')
    postcode2 = input('Enter the second postcode: ')
    postcode3 = input('Enter the third postcode: ')

    dictionary_post_codes = {
        'postcodes': [postcode1, postcode2, postcode3] }
    json_body = json.dumps(dictionary_post_codes)
    postcodes_post_response = requests.post(base_url+path, data=json_body, headers=headers)

    # print(postcodes_post_response.json())
    results = postcodes_post_response.json()['result']
    for request in results:
        print(f"Postcode: {request['result']['postcode']} with nhs location at: {request['result']['nhs_ha']}")


def get_lat_long():
    postcode = input('Enter the postcode: ')
    #make dictionary
    dictionary_post_codes = {
        'postcodes': [postcode]}
    json_body = json.dumps(dictionary_post_codes)
    lat_long_post_response = requests.post(base_url + path, data=json_body, headers=headers)
    results = lat_long_post_response.json()['result']
    for request in results:
        print(f"Latitude: {request['result']['latitude']} Longitude: {request['result']['longitude']}")

get_lat_long()


    # print('postcode: with nhs location at', + nhs_location)

    # ## Task
    # Make a small program that requests 3 postcodes and returns something
    # like:
    # '''
    #    > 1 - Postcode: xyzpto with nhs location at: xyx
    #    > 2 - Postcode: xyzpto2 with nhs location at: xyx
    #    > 3 - (....)
    # '''

    # Then you should also create some code to get out the Lat and Long
    # This should now start to be into functions