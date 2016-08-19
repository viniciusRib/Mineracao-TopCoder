# coding=utf-8
def forum_not_rank():

	merge_list = []
	list_merge_rank = []
	list_top_50_forum = []

	arquivo_total = open('forum_not_rank.txt', 'w')

	with open("merge_rank.txt", mode='r', buffering=1) as lines:
	    for line in lines:
	    	list_merge_rank.append(line)

	with open("top_50_forum.txt", mode='r', buffering=1) as lines:
	    for line in lines:
	    	list_top_50_forum.append(line)
	    	
	for i in range(len(list_top_50_forum)):
		if list_top_50_forum[i] not in list_merge_rank:
			arquivo_total.write("%s" % list_top_50_forum[i])

forum_not_rank()

