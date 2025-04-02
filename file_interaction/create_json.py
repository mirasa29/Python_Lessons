import json
import os

infiledir = f'{os.path.abspath(os.curdir)}/in'
outfiledir = f'{os.path.abspath(os.curdir)}/out'

# Define the data for the Yellowstone series
yellowstone_data = {
    "title": "Yellowstone",
    "seasons": 4,
    "episodes": {'season1': 9, 'season2': 10, 'season3': 10, 'season4': 10},
    "main_cast": {"father": "Kevin Costner", "son": "Luke Grimes", "daughter": "Kelly Reilly"},
    "genre": "Drama"
}

# Path to the JSON file
json_file_path = f'{infiledir}/yellowstone_series.json'

# Write the data to the JSON file
with open(json_file_path, 'w', encoding='utf-8') as jsonfile:
    json.dump(yellowstone_data, jsonfile, indent=4)

