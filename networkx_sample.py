import networkx as nx
import string

#new graph
G = nx.Graph()

#add node
G.add_node("A")
#number of node 
print(nx.number_of_nodes(G))

#addable list
G.add_nodes_from(string.ascii_uppercase)
print(nx.number_of_nodes(G))

#add egde
G.add_edge("A","B")
#number of edge
print(nx.number_of_edges(G))

#addable list
list_edge = [("C","D"),("E","F"),("G","H")]
G.add_edges_from(list_edge)
print(nx.number_of_edges(G))
