from collections import Counter
import itertools
import operator

def most_common(L):
  words_counts = Counter(L)
  top_100 = words_counts.most_common(100)
  return top_100

def get_list():

  lista = []

  with open('output_fix.txt') as f:
    for line in f:
      aux = line.split(' ')
      lista.append(aux[0])
  return lista
      

def write_file_common():
  arquivo = open("common_final.txt", "w")      
  aux = str(most_common(get_list())).replace('(', '').replace(')', '').replace('\'', '').replace('[', '').replace(']', '').replace(',', '')
  aux2 = aux.split(' ')

  for i, j in zip(aux2[0::2], aux2[1::2]):
    arquivo.write('membro: %s ' % str(i) + '--> %s' % str(j))
    arquivo.write("\n")

write_file_common()
