import os
import pandas as pd
import pprint
import datetime

if not os.path.exists('extracts'):
    os.makedirs('extracts')

fileName = input('Please enter your filename (without .csv extension): ')

places = pd.read_csv(f'datas/{fileName}.csv', sep= ';', usecols=['name', 'com_insee', 'com_nom'], encoding='utf-8')

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

with open (f'extracts/extract-{fileName}.py', 'w', encoding="utf-8") as extracted:
    extracted.write(f'# Generated at {current_time} \n')
    extracted.write(pprint.pformat(placesList))

print('---')
print(f'{labelCount} labeled places out of {len(places)} rows found.')
print(f'File : "extracts/extract-{fileName}.py" created with success.')