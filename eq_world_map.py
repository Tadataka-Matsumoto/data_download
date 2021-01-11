import json

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

#データの構造を調査する(p147)(p155)
filename = 'data/eq_data_30_day_m1.json'
with open(filename) as f:
    all_eq_data = json.load(f)#pythonで使える形式に変える関数(p147)

all_eq_dicts = all_eq_data['features']#地震データのfeatureキーを取り出す(p149)
# print(len(all_eq_dicts))

mags, lons, lats, hover_texts = [], [], [], []#hover_textはp157で追加
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    title = eq_dict['properties']['title']#p157ホバーテキストで追加
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)
    hover_texts.append(title)

#地震の地図(p155)もともとp151
# data = [Scattergeo(lon=lons, lat=lats)]#p121参照(角カッコじゃないとダメ)(p151)
data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': hover_texts,
    'marker': {
        'size': [5*mag for mag in mags],
        'color':mags,
        'colorscale': 'Viridis',#これが一番いいと思う
        # 'colorscale': 'Rainbow',#p156参照
        # 'colorscale': 'Portland',#p156参照
        'reversescale': True,
        'colorbar': {'title': 'マグニチュード'},
    },
}]#表現を最小限の書き方から変更と、キー（marker）を追加(p153)

my_layout = Layout(title='世界の地震')

fig = {'data':data, 'layout':my_layout}
offline.plot(fig, filename='global_earthquakes.html')