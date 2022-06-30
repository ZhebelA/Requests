from pprint import pprint
import requests

url = 'https://akabab.github.io/superhero-api/api/all.json'
all = requests.get(url)
# pprint(all)

intel_list = {}
for hero in all.json():
    if hero['name'] == 'Hulk' or hero['name'] == 'Captain America' or hero['name'] == 'Thanos':
        # pprint(f'intelligence of {hero["name"]} = {hero["powerstats"]["intelligence"]}')
        name = str(hero['name'])
        intel = int(hero["powerstats"]["intelligence"])
        intel_list[name] = intel
print(f'The most intelligent hero is {max(intel_list, key=intel_list.get)}')
