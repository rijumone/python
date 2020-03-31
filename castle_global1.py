def addNumbers(a,b):
		return [[a+b,b],[b,a+b]]
	
# a = int(raw_input())
a = 1
# b = int(raw_input())
b = 4
# c = int(raw_input())
c = 14
# d = int(raw_input())
d = 21


mainList = [[a,b]]

# print mainList

answerPossible = True

while answerPossible :
	# if a == c and b == d :
	# 	print 'Yes'
	# 	break
	mainList = mainList + addNumbers(mainList[len(mainList)-1][0],mainList[len(mainList)-1][1])
	# a = temp[0]
	# b = temp[1]
	# print mainList
	if mainList[len(mainList)-1][0] > c or mainList[len(mainList)-1][1] > d or mainList[len(mainList)-2][0] > c or mainList[len(mainList)-1][1] > d  :
		answerPossible = False

answerFound = False

for k,v in enumerate(mainList):
	if v[0] == c and v[1] == d:
		answerFound = True
		break

if answerFound:
	print "Yes"
else:
	print "No"