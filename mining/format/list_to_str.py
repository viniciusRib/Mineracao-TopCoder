arquivo = open("dataset3.txt", "w")
arquivo_read = open("dataset2.txt", "r")

lista = arquivo_read.readline()

while lista:
	lista = arquivo_read.readline() 
	aux = ''.join(map(str, lista))

	print aux

	aux2 = ''.join(aux)

	print aux2

	break
