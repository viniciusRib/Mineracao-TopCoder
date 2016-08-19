arquivo = open("./algorithm-generalposts.txt", "w")

for i in range(0, 7415, 15):
	arquivo.write("http://apps.topcoder.com/forums/?module=ThreadList&forumID=205768&sortField=9&sortOrder=0&start=%s" % i)
	arquivo.write("\n")

#arquivo_read = open("posts.txt", "r")
