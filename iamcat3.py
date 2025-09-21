import requests
from janome.tokenizer import Tokenizer
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# 青空文庫の『吾輩は猫である』テキストファイルのURL
url = "https://www.aozora.gr.jp/cards/000148/files/789_14547.html"

# テキストをダウンロード
response = requests.get(url)
response.encoding = "shift_jis"  # 青空文庫はShift-JISなので指定
text = response.text

# 余計なタグや注記をざっくり削除（HTMLタグを取り除く）
import re
text = re.sub(r"<[^>]*>", "", text)  # HTMLタグ削除
text = re.sub(r"《.*?》", "", text)   # ルビ削除
text = re.sub(r"［.*?］", "", text)   # 注記削除

# Janomeで形態素解析（名詞だけ抽出）
t = Tokenizer()
words = [token.base_form for token in t.tokenize(text) if token.part_of_speech.startswith("名詞")]

# スペース区切りに変換
text_processed = " ".join(words)

# フォントパスを指定（環境に合わせて変更してください）
# Windows: "C:\\Windows\\Fonts\\msgothic.ttc"
# Mac: "/System/Library/Fonts/ヒラギノ明朝.ttc"
# Linux: "/usr/share/fonts/truetype/ipafont/ipagp.ttf"
font_path = "C:\\Windows\\Fonts\\msgothic.ttc"

# ワードクラウド生成
wordcloud = WordCloud(width=800, height=400, background_color="white", font_path=font_path).generate(text_processed)

# 表示
plt.figure(figsize=(12, 6))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()
