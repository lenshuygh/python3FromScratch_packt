import requests
r = requests.get('http://www.opzoeken-postcode.be/2000.json').json()
print(len(r))

