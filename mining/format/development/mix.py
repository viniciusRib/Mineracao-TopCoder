# coding=utf-8

common = 'common_final.txt'
top_50 = 'top_50.txt'

arquivo = open('top_50_names.txt', 'w')

lista1 = []
lista2 = []

with open(common, mode='r', buffering=1) as lines:
    for line in lines:
    	lista1.append(line)

with open(top_50, mode='r', buffering=1) as lines:
    for line in lines:
    	lista2.append(line)

for i in range(1, len(lista1)):
	aux = lista1[i], lista2[i]
	string = str(aux)
	arquivo.write("%s\n" % string)