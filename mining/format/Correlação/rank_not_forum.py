# coding=utf-8
def rank_not_forum():

	merge_list = []
	list_merge_rank = []
	list_top_50_forum = []
	list_rank_not_forum = []
	list_both = []

	arquivo_total = open('rank_not_forum.txt', 'w')

	with open("merge_rank.txt", mode='r', buffering=1) as lines:
	    for line in lines:
	    	list_merge_rank.append(line)

	with open("top_50_forum.txt", mode='r', buffering=1) as lines:
	    for line in lines:
	    	list_top_50_forum.append(line)

	with open("both.txt", mode='r', buffering=1) as lines:
	    for line in lines:
	    	list_both.append(line)
	    	
	for i in range(len(list_merge_rank)):
		if list_merge_rank[i] not in list_top_50_forum:
			list_rank_not_forum.append(list_merge_rank[i])

	for i in range(len(list_rank_not_forum)):
		if list_rank_not_forum[i] not in list_both:
			arquivo_total.write("%s" % list_rank_not_forum[i])

rank_not_forum()



