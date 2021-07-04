import MeCab
#MeCab を import
#i_am_cat.txt を読み込んで分かち書きする
with open('/media/takuma/NORITAMA/工学実験Ⅳ/Part3/i_am_a_cat.txt','r',encoding='utf-8')as f:
    text = f.read()
    m = MeCab.Tagger("-Ochasen") #オブジェクトを作成
    node = m.parseToNode(text) #形態素情報を取得
    count = 0
    while node: #繰り返し
        word = node.feature.split(",")[6] #原型を取得
        type = node.feature.split(",")[0] #品詞を取得
        if type in ('動詞'): #品詞が名詞なら原型を表示
            print(node.feature)
            print(word)
            count += 1
        if(count ==10):
            break
        node = node.next
        #次の node へ