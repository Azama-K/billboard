import pandas as pd # pandasのインポート
from bs4 import BeautifulSoup # BeautifulSoupのインポート
import requests # requestsのインポート
import collections # collectionsのインポート

url = "https://www.billboard.com/charts/hot-100"

# requestsで、指定されたURLのHTMLを取得する。
response = requests.get(url).text

# requestsで取得したHTMLをBeautifulSoupで呼び出す。
soup = BeautifulSoup(response, 'html.parser') # BeautifulSoupの初期化

# classを取得
tags_song = soup.find_all("span",{"class":"chart-element__information__song"})
tags_artist = soup.find_all("span",{"class":"chart-element__information__artist"})

# データフレームを作成。
columns = ["rank", "song", "artist"]
df2 = pd.DataFrame(columns=columns)

# 記事名と記事URLをデータフレームに追加する。
for i in range(100):
    song = tags_song[i].getText()
    artist = tags_artist[i].getText()
    num = i+1
    se = pd.Series([num, song, artist], columns)
    df2 = df2.append(se, columns)

# CSVに出力。
filename = "CSV_billboard.csv"
# df2.to_csv(filename, encoding = 'utf-8-sig') #encoding指定しないと、エラーが起こる。
# print(df2)

#ベスト100の中でこのartistが何回ランクインしたかを表示(featuringも適切に対処)
a = []
for i in df2['artist']: # artist名で検索
    if "&" in i: # &が出ている時の対処
        d = i.split("&")
        for j in d:
            a.append(j.strip())
    elif "Featuring" in i:
        d = i.split("Featuring")
        print(i)
        for j in d:
            a.append(j.strip())
    elif "X" in i:
        d = i.split("X")
        for j in d:
            a.append(j.strip())
    elif "With" in i:
        d = i.split("With")
        for j in d:
            a.append(j.strip())
    elif "+" in i:
        d = i.split("+")
        for j in d:
            a.append(j.strip())
    else:
        a.append(i)

b = df2['artist']
c = collections.Counter(a)



print(a.count('Ariana Grande'))
# print(b[1])
print(c)







