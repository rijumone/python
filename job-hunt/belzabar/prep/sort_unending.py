mainList = []

q = int(raw_input())

while q:
	if not mainList:
		mainList.append(q)
	for p in range(0,len(mainList)):
		# print mainList[p+1]
		print p
		print mainList
		if 0 <= p + 1  < len(mainList) and mainList[p] > q and  mainList[p+1] < q:
			mainList.insert(p,q)
		
	print mainList
	q = int(raw_input())