import requests
# Get request
# Do not have a body (JSON)
# They have a base url, path and arguments

# api.postcodes.io/postcodes/ (contains base url and path)
base_url = 'http://api.postcodes.io/'
path = 'postcodes/'
arguments = 'e146gt'

request_response = requests.get(base_url+path+arguments)
print(request_response)

#Turning a request to a dictionary using json --> use .json
dictionary_response = request_response.json()
print(dictionary_response)
print(dictionary_response['result']['admin_ward'])



# ## Task
# Make a small program that requests 3 postcodes and returns something
# like:
# '''
#    > 1 - Postcode: xyzpto with nhs location at: xyx
#    > 2 - Postcode: xyzpto2 with nhs location at: xyx
#    > 3 - (....)
# '''
