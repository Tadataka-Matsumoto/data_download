import json

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

#データの構造を調査する(p147)
filename = 'data/eq_data_1_day_m1.json'
with open(filename) as f:
    all_eq_data = json.load(f)#pythonで使える形式に変える関数(p147)

#print(all_eq_data)#お試し

all_eq_dicts = all_eq_data['features']#地震データのfeatureキーを取り出す(p149)
# print(len(all_eq_dicts))

# mags = []#p150
# for eq_dict in all_eq_dicts:
#     mags.append(eq_dict['properties']['mag'])

# print(mags[:10])

mags, lons, lats = [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)

print(mags[:10])
print(lons[:5])
print(lats[:5])


readable_file = 'data/readable_eq_data.json'
with open(readable_file, 'w') as f:
    json.dump(all_eq_data, f, indent=4)


#地震の地図(p151)
# data = [Scattergeo(lon=lons, lat=lats)]#p121参照(角カッコじゃないとダメ)(p151)
data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'marker': {
        'size': [5*mag for mag in mags],
    },
}]#表現を最小限の書き方から変更と、キー（marker）を追加(p153)


my_layout = Layout(title='世界の地震')

fig = {'data':data, 'layout':my_layout}
offline.plot(fig, filename='global_earthquakes.html')