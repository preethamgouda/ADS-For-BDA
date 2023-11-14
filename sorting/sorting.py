def _swap(input, idx1, idx2):
	input[idx1], input[idx2] = input[idx2], input[idx1]

def testSorting(input):
	for idx in range(0, len(input)-1):
		assert(input[idx] <= input[idx+1])

def bubbleSort(input):
	for itr in range(0, len(input) - 2):
		for idx in range(len(input)-1, itr, -1):
			if input[idx] < input[idx-1]:
				input[idx], input[idx-1] = input[idx-1], input[idx]
	testSorting(input)

def selectionSort(input):
	for itr in range(0, len(input)-2):
		pos = itr
		for idx in range(itr+1, len(input)):
			if input[idx] < input[pos]:
				pos = idx
		_swap(input, itr, pos)
		
	
	testSorting(input)



	