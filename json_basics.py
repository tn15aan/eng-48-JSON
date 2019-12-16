import json


car_dictionary = {
    'name': 'tesla',
    'engine': '90000kj',
    'type': 'electric'
}

print(type(car_dictionary))
print(car_dictionary)

#Use this to create JSON string from our dictionaries on the go
# json.dumps(dict_obj) --> string
car_data_json_string = json.dumps(car_dictionary)
print(type(car_data_json_string))
print(car_data_json_string)

# json.dump(dict_object, file) --> writes json to a file
# a new file will be created here including the string
with open('new_json_file.json', 'w') as jsonfile:
    json.dump(car_dictionary, jsonfile)

