from janome.tokenizer import Tokenizer
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# 日本語サンプルテキスト（青空文庫からの冒頭抜粋）
text = """
吾輩は猫である。名前はまだ無い。どこで生れたかとんと見当がつかぬ。
何でも薄暗いじめじめした所でニャーニャー泣いていた事だけは記憶している。
吾輩はここで始めて人間というものを見た。
しかもあとで聞くとそれは書生という人間中で一番獰悪な種族であったそうだ。
"""

# Janomeで形態素解析（名詞を抽出）
t = Tokenizer()
words = [token.base_form for token in t.tokenize(text) if token.part_of_speech.startswith("名詞")]

# スペース区切りに変換
text_processed = " ".join(words)

# 日本語フォントのパスを指定（環境に合わせて変更してください）
# Windowsの場合の例: "C:\\Windows\\Fonts\\msgothic.ttc"
# Macの場合の例: "/System/Library/Fonts/ヒラギノ明朝.ttc"
# Linuxの場合の例: "/usr/share/fonts/truetype/ipafont/ipagp.ttf"
font_path = "C:\\Windows\\Fonts\\msgothic.ttc"

# ワードクラウド生成
wordcloud = WordCloud(width=800, height=400, background_color="white", font_path=font_path).generate(text_processed)

# 表示
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()
