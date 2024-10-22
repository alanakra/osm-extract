import pandas as pd
import pprint
import datetime

places = pd.read_csv('datas/data-sport-77.csv', sep= ';', usecols=['name', 'com_insee', 'com_nom'], encoding='utf-8')

labelCount = 0

placesList = set()
current_time = datetime.datetime.now()

for _, row in places.iterrows():
    name = row['name']
    insee = row['com_insee']
    commune = row['com_nom']
    if not pd.isna(name):
        placesList.add((name, insee, commune))
        labelCount += 1
        print('---')
        print(name)
        print(insee)
        print(commune)

with open (f'extracts/extract-77.py', 'w', encoding="utf-8") as extracted:
    extracted.write(f'# Generated at {current_time} \n')
    extracted.write(pprint.pformat(placesList))

print('---')
print(f'{labelCount} labeled places out of {len(places)} rows found.')