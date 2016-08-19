# coding=utf-8
def both():

	merge_list = []
	list_total = []
	list_top_design = []
	list_top_development = []
	list_top_50 = []

	arquivo_total = open('both.txt', 'w')

	with open("rank_nomes_design.txt", mode='r', buffering=1) as lines:
	    for line in lines:
	    	list_top_design.append(line)

	with open("rank_nomes_development.txt", mode='r', buffering=1) as lines:
	    for line in lines:
	    	list_top_development.append(line)

	caminho = "/home/vinicius/Documents/6ºPeríodo/Mineração de Repositórios de Software/tutorial/aux/development/top_50.txt"

	with open(caminho, mode="r", buffering=1) as lines:
		for line in lines:
			list_top_50.append(line)

	merge_list = list_top_design + list_top_development

	merge_list_no_duplicate = list(set(merge_list))

	arquivo_merge = open('merge_rank.txt', 'w')
	
	for i in range(len(merge_list_no_duplicate)): 
	   	arquivo_merge.write("%s" % merge_list_no_duplicate[i])	    	

	for i in range(len(merge_list_no_duplicate)):
		if merge_list_no_duplicate[i] in list_top_50:
			arquivo_total.write("%s" % merge_list_no_duplicate[i])
			

both()

