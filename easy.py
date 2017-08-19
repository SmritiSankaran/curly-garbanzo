#code = ["ATGC", "A", "TT", "CACTAT","TT"]
#final = []
#shortest = code[0]
#while len(code) > 0:
#	for each in code:
#		if len(each) < len(shortest):
#			shortest = each
#	final.append(shortest)
#	code.remove(shortest)
#	if len(code) > 0:	
#		shortest = code[0]
#print(final)

code = ["ATGC", "A", "TT", "CACTAT","TT"]
shortest = code[0]
while len(code) > 0:
       for each in code:
               if len(each) < len(shortest):
                       shortest = each
	blah = code[0]
	code.remove(shortest)
       	code[0] = shortest
	code.append(blah)
	if len(code) > 0:
		shortest = code[0]
print (code)
