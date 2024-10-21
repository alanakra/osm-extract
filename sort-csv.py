import pandas as pd

places = pd.read_csv('datas/data-sport-77.csv', sep= ';', usecols=['name', 'com_insee', 'com_nom'], encoding='utf-8')

labelCount = 0

placesList = set()

for _, row in places.iterrows():
    name = row['name']
    post = row['com_insee']
    commune = row['com_nom']
    if not pd.isna(name):
        placesList.add((name, post, commune))
        labelCount += 1
        print('---')
        print(name)
        print(post)
        print(commune)
        print(placesList)

print(f'{labelCount} labeled places out of {len(places)} rows found.')