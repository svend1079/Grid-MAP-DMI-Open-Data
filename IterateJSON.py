import json
import codecs

with open("Municipalities/Municipalities.geojson", 'r') as f:
    data = json.load(f)

for munic in data['features']:
    munic['properties']['MunicipalityId'] = '0' + str(munic['properties']['MunicipalityID'])

with codecs.open('Municipalities/Municipalities.geojson', 'w') as f:
    json.dump(data, f)