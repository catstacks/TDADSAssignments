# Make a request to the Electricity Costs API

import requests

headers = {'Accept': 'application/json'}

r = requests.get('https://odegdcpnma.execute-api.eu-west-2.amazonaws.com/development/prices?dno=10&voltage=HV&start=01-06-2021&end=03-06-2021', params={}, headers = headers)

print(r.json())

