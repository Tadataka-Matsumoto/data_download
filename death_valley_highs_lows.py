import csv#p142
from datetime import datetime#p 

import matplotlib.pyplot as plt

filename = 'data/death_valley_2018_simple.csv'#p141
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)


    # for index, column_header in enumerate(header_row):#p141で最高気温と最低気温の位置が違うことを確認
    #     print(index, column_header)

    #ファイルから日付、最高気温、最低気温を取得する
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        try:#p142で追加！！
            high = int(row[4])
            low = int(row[5])
        except ValueError:#p142で追加！！
            print(f"Missing data for {current_date}")
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)


#最高気温のグラフを描画する
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

#グラフのフォーマットを指定する
# plt.title("Daily high temperatures, July 2018", fontsize=24)
title = "Daily high and low temperatures - 2018\nDeath Valley, CA"
plt.title(title, fontsize=20)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()#p136の説明（x軸が川成合わない容易に斜めに表示）
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()