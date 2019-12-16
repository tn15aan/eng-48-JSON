import json

# Defining the dictionary
car_dictionary = {
    'name': 'tesla',
    'engine': '90000kw',
    'type': 'electric'
}

print(type(car_dictionary))
print(car_dictionary)

#Use this to create JSON string from our dictionaries on the go
# json.dumps(dict_obj) --> string
car_data_json_string = json.dumps(car_dictionary)
print(type(car_data_json_string)) # Checking the different types dict and now should be string
print(car_data_json_string)

# json.dump(dict_object, file) --> writes json to a file
# The new file will be created 'new_json_file.json' (without me manually doing it) and outputs the string
with open('new_json_file.json', 'w') as jsonfile:
    json.dump(car_dictionary, jsonfile)

#json.load(jsonfile) ----> dictionary
# Loading it as a dictionary again to read it
with open('new_json_file.json', 'r') as jsonfile:
    car = json.load(jsonfile)
    print(type(car))
    print(car['engine']) # Getting value of car's engine in the dictionary

