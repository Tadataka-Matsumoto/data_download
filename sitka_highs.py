import csv#p131
from datetime import datetime #datetimeモジュールp135(正式にはp136)

import matplotlib.pyplot as plt#p133で追加

# filename = 'data/sitka_weather_07-2018_simple.csv'#短いスパンのデータ用p131
filename = 'data/sitka_weather_2018_simple.csv'#長いスパンのデータ用p137
with open(filename) as f:
    reader = csv.reader(f)#csvファイルに関連付けられた読み込みオブジェクトを生成(p131)
    header_row = next(reader)#csvファイルの最初の行が読み込まれる(p131)
    # print(header_row)#p131

    # for index, column_header in enumerate(header_row):#データの最初の行をindexとともに出力(p132)
    #     print(index, column_header)

    #ファイルから日付、最高気温、最低気温を取得する(p133, p138)
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')#p136
        high = int(row[5])#p133
        low = int(row[6])#p138
        dates.append(current_date)#p136
        highs.append(high)
        lows.append(low)#p138

# print(highs,lows)#p133

    # ttt = datetime.strptime("2018-11-11", '%Y-%m-%d')   #試し(p135)
    # print(ttt)#試し


#最高気温のグラフを描画する(p134)
plt.style.use('seaborn')#p133
fig, ax = plt.subplots()#p133
ax.plot(dates, highs, c='red', alpha=0.5)#p133,p140でalphaを追加(0は透明、1は鮮明)
ax.plot(dates, lows, c='blue', alpha=0.5)#p139で追加
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)#隙間を埋める(p140)

#グラフのフォーマットを指定する(p134)
# plt.title("Daily high temperatures, July 2018", fontsize=24)#p134
plt.title("Daily high and low temperatures - 2018", fontsize=24)#p137
plt.xlabel('', fontsize=16)#p134
fig.autofmt_xdate()#p136の説明（x軸が重なり合わない用に斜めに表示）
plt.ylabel("Temperature (F)", fontsize=16)#p134
plt.tick_params(axis='both', which='major', labelsize=16)#p134(p99とp103参照)

plt.show()