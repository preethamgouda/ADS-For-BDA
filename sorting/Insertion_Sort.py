def testSorting(input):
	for idx in range(0, len(input)-1):
		assert(input[idx] <= input[idx+1])


def insertionSort(input):
	for itr in range(1, len(input)):
		idx = itr - 1
		key = input[itr]
		while idx >= 0 and key < input[idx]:
			input[idx+1] = input[idx]
			idx -= 1
		input[idx+1] = key
	testSorting(input)