import json
from pprint import pprint

with open('data.json') as data_file:
    data = json.load(data_file)

with open('dataDump.json', 'w') as f:
    json.dump(data, f)

pprint(data)