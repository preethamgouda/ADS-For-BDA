def mergeSort(mylist):
	if len(mylist) == 0 or len(mylist) == 1:
		return mylist
	else:
		mid = len(mylist)//2
		a = mergeSort(mylist[:mid])
		b = mergeSort(mylist[mid:])
		return merge(a, b)

def merge(a, b):
	temp_list = []

	while len(a) != 0 and len(b) != 0:
		if a[0] < b[0]:
			temp_list.append(a[0])
			a.pop(0)
		else:
			temp_list.append(b[0])
			b.pop(0)
	if len(a) == 0:
		temp_list = temp_list + b
	else:
		temp_list = temp_list + a

	return temp_list

def test_mergeSort():
	sorted_list = mergeSort([29, 45, 12,9, 23, 56, 90, 60 ,30])
	#print(sorted_list)
	for idx in range(len(sorted_list)-1):
		assert(sorted_list[idx] <= sorted_list[idx+1])

test_mergeSort()