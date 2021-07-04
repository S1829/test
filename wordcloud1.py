from wordcloud import WordCloud #WordCloud を import
import matplotlib.pyplot as plt #matplotlib.pyplot を import
import MeCab #Mecab を import
from bs4 import BeautifulSoup #BeautifulSoup を import
import requests #requests を import
FONT = "./media/takuma/NORITAMA/IPAexfont00401/ipaexg.ttf"
#フォントのファイルを定義
stop_words = [u'れ', u'てる', u'いる', u'なる', u'れる', u'する', u'ある', u'こと', u'これ', u'さん', u'して', u'くれる', u'やる', u'くださる', u'そう', u'せる', u'した', u'思う', u'それ', u'ここ', u'ちゃん', u'くん', u'', u'て', u'ない']
#除去ワードリスト
url = "http://www.oita-ct.ac.jp/gakucho/"
#url を定義
html = requests.get(url).content #url から HTML を取得
soup = BeautifulSoup(html, 'html.parser') #BeautifulSoup オブジェクトを作成
text = soup.find(class_='wp-block-columns').get_text()
#テキストのみ取得
mecab = MeCab.Tagger('-Owakati') #オブジェクトを定義
node = mecab.parseToNode(text) #形態素情報を取得
words = []
while (node):
    #繰り返し
    word_type = node.feature.split(',')[0] #品詞を取得
    word = node.feature.split(',')[6] #原型を取得
    if word_type in ["形容詞", "動詞", "名詞", "副詞"]: #word_type が一致したとき真
        if not word_type in ('*'):
            #「*」は除く
            words.append(word)
            #word に追加
    node = node.next
    #次の node へ
word_str = ' '.join(words)
#リストを一つの文字列に連結する
wordcloud=WordCloud(background_color="black",width=900,height=500,font_path=FONT,stopwords=set(stop_words)).generate(word_str)

#WordCloud オブジェクトを作成#plt を使用して頻出度を可視化させる
plt.figure(figsize=(15, 12))
plt.imshow(wordcloud)
plt.axis("off")
plt.show()