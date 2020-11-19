import pandas as pd # pandasのインポート
from bs4 import BeautifulSoup # BeautifulSoupのインポート
import requests # requestsのインポート

url = "https://www.billboard.com/charts/hot-100"

# requestsで、指定されたURLのHTMLを取得する。
response = requests.get(url).text

# requestsで取得したHTMLをBeautifulSoupで呼び出す。
soup = BeautifulSoup(response, 'html.parser') # BeautifulSoupの初期化

# classを取得
tags_song = soup.find_all("span",{"class":"chart-element__information__song"})
tags_artist = soup.find_all("span",{"class":"chart-element__information__artist"})

# データフレームを作成。列名は、name, url。
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
df2.to_csv(filename, encoding = 'utf-8-sig') #encoding指定しないと、エラーが起こる。
