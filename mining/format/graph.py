#!/usr/bin/env python

from collections import Counter
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib
import pylab

arquivo_weight = open("nomes_weight.txt", "w+")

edge_counts = Counter((' '.join(line.strip().split('; ')[0:]) for line in open('nomes_aux.txt') if not line.startswith('#')))

G = nx.parse_edgelist(('%s %d' % edge for edge in edge_counts.items()),
	data=(('weight',int),),
    create_using=nx.DiGraph())

nx.draw(G)
#plt.show()

from pprint import pprint

with open('output.txt', 'wt') as out:
    pprint(sorted(G.edges(data=True)), stream=out)
