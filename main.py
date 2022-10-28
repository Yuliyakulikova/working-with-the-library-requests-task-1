from pprint import pprint
import requests

url = 'https://akabab.github.io/superhero-api/api/all.json'
resp = requests.get(url)
a = (resp.json())
intelligence_dict = {'Hulk': 0, 'Captain America': 0, 'Thanos': 0}
for a1 in a:
    if a1['name'] == 'Hulk':
        Thanos = (a1)
        intelligence_dict['Hulk'] = int(Thanos['powerstats']['intelligence'])

for a1 in a:
    if a1['name'] == 'Thanos':
        Thanos = (a1)
        intelligence_dict['Thanos'] = int(Thanos['powerstats']['intelligence'])

for a1 in a:
    if a1['name'] == 'Captain America':
        Captain_America = (a1)
        intelligence_dict['Captain America'] = int(Captain_America['powerstats']['intelligence'])

print("Самый умный из 3-х супергероев:", max(intelligence_dict))

