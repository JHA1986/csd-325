# Jonah Aney CSD325 Module 9.2 Assignment: APIs
# #6-simple APIs - pokeAPI

import requests
# making a GET request
response = requests.get("https://pokeapi.co/api/v2/berry/cheri")
# view the data
print(response.json())

# import JSON library
import json
# create a formatted string of the python JSON object
def jprint(odj):
   text = json.dumps(odj, sort_keys=True, indent=4)
   print(text)

jprint(response.json())







