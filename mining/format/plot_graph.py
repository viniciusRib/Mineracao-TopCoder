from igraph import *
import networkx as nx
import matplotlib.pyplot as plt

'''G = nx.read_edgelist("output_graph.txt", delimiter=",", data=[("weight", int)])

edge_labels = dict( ((u, v), d["weight"]) for u, v, d in G.edges(data=True))
pos = nx.random_layout(G)
nx.draw(G, pos)
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

plot(G, 'teste.png', (800, 600))

#plt.show()'''

g = Graph()

#arquivo2 = open("lalala.txt", "r")

names_graph = g.Read_Ncol("output_graph.txt", directed=False)

names_graph.write("names1.gml", format="gml")

#print names_graph.assortativity()

#plot(names_graph)

