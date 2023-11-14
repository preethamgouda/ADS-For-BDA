def quickSort(mylist):
	start = 0
	end = len(mylist) - 1
	l1 =_quick_sort_(mylist, start, end)
	print (l1)
	#_test_sort_(mylist)


def _quick_sort_(mylist, start, end):
	
	#l1=[]
	if start < end:
		mid = _partition_(mylist, start, end)
		_quick_sort_(mylist, start, mid-1)
		_quick_sort_(mylist, mid+1, end)
	return mylist

def _partition_(mylist, start, end):
	up = start
	pivot = mylist[start]
	down = end

	while up <= down:
		while up <= down and mylist[up] <= pivot:
			up += 1
		while up <= down and mylist[down] > pivot:
			down -= 1

		if up <= down:
			mylist[up], mylist[down] = mylist[down], mylist[up]

	mylist[start], mylist[down] = mylist[down], mylist[start]

	return down

def _test_sort_(mylist):
	for idx in range(0, len(mylist)-1 ):
		assert(mylist[idx] <= mylist[idx+1])

def test_quickSort():
	quickSort([35, 20, 45, 15, 98, 9, 67, 75, 16, 30, 60])

test_quickSort()

