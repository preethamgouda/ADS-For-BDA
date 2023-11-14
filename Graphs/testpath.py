def testPaths(l1):		
	indicies = getAllIndicies(l1)	# get hold of all indices of 'element'  from list	
	paths = []
	for idx in range(len(indicies)):
		if indicies[idx] != indicies[-1]: # to exclude the last value in list indicies
			paths.append(l1[indicies[idx]:indicies[idx+1]])
	
	paths.append(l1[indicies[-1]:]) # last value from indicies is added outside loop
	return paths

def getAllIndicies(l1):
	indicies = [ i for i in range(len(l1)) if l1[i] == l1[0]]
	return indicies


print (testPaths(['a', 'b', 'e', 'a', 'e', 'a', 'c', 'e']))
