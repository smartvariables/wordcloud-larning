import requests
from janome.tokenizer import Tokenizer
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import re

# 青空文庫の「銀河鉄道の夜」のURL
url = "https://www.aozora.gr.jp/cards/000081/files/456_15050.html"

# テキストを取得
response = requests.get(url)
response.encoding = "shift_jis"  # 青空文庫の多くはShift-JIS
text = response.text

# HTMLタグや注記を取り除く
# タグ削除
text = re.sub(r"<[^>]*>", "", text)
# ルビ・振り仮名などの注記削除
text = re.sub(r"《.*?》", "", text)
text = re.sub(r"［.*?］", "", text)
# 前書き・あとがきなど不要部分も取り除きたいならこの辺りで加工

# 形態素解析：名詞を抽出
t = Tokenizer()
words = [token.base_form for token in t.tokenize(text) if token.part_of_speech.startswith("名詞")]

# スペース区切りに変換
text_processed = " ".join(words)

# フォントパス（ご自身のPC環境に応じて変更してください）
# 例：Windows 用
font_path = "C:\\Windows\\Fonts\\msgothic.ttc"
# 例：Mac 用
# font_path = "/System/Library/Fonts/ヒラギノ明朝.ttc"
# 例：Linux 用
# font_path = "/usr/share/fonts/truetype/ipafont/ipagp.ttf"

# ワードクラウドを作る
wordcloud = WordCloud(width=800, height=400, background_color="white", font_path=font_path).generate(text_processed)

# 表示
plt.figure(figsize=(12, 6))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()

