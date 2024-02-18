import json
with open('config.json', 'r') as file:
    data = json.load(file)
# constants
token = data['TOKEN']
prefix = data['PREFIX']
