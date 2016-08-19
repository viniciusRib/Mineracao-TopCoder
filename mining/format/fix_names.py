# coding=utf-8
import itertools

arquivo = open("nomes_aux.txt", "w+")

caminho = "nomes.txt"

aux = []
line_split = []

with open(caminho, mode='r', buffering=1) as lines:
    for line in lines:
		line_replace = line.replace('[', '').replace(']', '').replace('\'', '').replace(',', '')
		line_split = line_replace.split()
		#print line_split
		lista_no_repeat = list(set(line_split))
		#print lista_no_repeat
		for i in itertools.permutations(lista_no_repeat, 2):
			aux = list(i)
			x = aux[0]
			
			y = aux[1]
			
			arquivo.write("%s" % x)
			arquivo.write(" %s" % y)
			arquivo.write("\n")
