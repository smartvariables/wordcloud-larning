# 必要なライブラリのインポート
import requests
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# オンラインのテキストデータのURLを指定
url = "https://www.gutenberg.org/files/11/11-0.txt"  # 不思議の国のアリス

# URLからテキストを取得
response = requests.get(url)
text = response.text

# ワードクラウドを生成する
wordcloud = WordCloud(width=800, height=400, background_color="white").generate(text)

# ワードクラウドを表示する
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()
