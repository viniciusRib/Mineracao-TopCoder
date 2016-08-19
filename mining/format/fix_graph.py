arquivo = open("output_fix.txt", "w+")

with open("output.txt", mode='r', buffering=1) as lines:
    for line in lines:
    	#print line
		line_replace = line.replace('}),', '').replace(' (\'', '').replace('{\'weight\':', '').replace(',', '').replace('\'', '').replace('(','')
		arquivo.write("%s" % line_replace)

