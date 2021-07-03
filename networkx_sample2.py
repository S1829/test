import networkx as nx
import matplotlib.pyplot as plt
 
G = nx.read_edgelist('/home/takuma/ドキュメント/edgelist.txt', nodetype=str)
 
# ノード数とエッジ数を出力
print(nx.number_of_nodes(G))
print(nx.number_of_edges(G))
 
#図の作成。figsizeは図の大きさ
plt.figure(figsize=(10, 8))
 
#図のレイアウトを決める。kの値が小さい程図が密集する
pos = nx.spring_layout(G, k=0.8)
 
#ノードとエッジの描画
# _color: 色の指定
# alpha: 透明度の指定
nx.draw_networkx_edges(G, pos, edge_color='y')
nx.draw_networkx_nodes(G, pos, node_color='r', alpha=0.5)
 
#ノード名を付加
nx.draw_networkx_labels(G, pos, font_size=10)
 
#X軸Y軸を表示しない設定
plt.axis('off')
 
#図を描画
plt.show()