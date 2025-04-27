# Jonah Aney CSD325 Module 9.2 Assignment: APIs

# import request library for API requests
import requests
# making a GET request
response = requests.get("http://api.open-notify.org/astros")
# view the data
print(response.json())


# import JSON library
import json
# create a formatted string of the python JSON object
def jprint(odj):
   text = json.dumps(odj, sort_keys=True, indent=4)
   print(text)

jprint(response.json())


