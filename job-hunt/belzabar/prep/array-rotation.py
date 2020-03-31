# Program for array rotation
# Write a function rotate(ar[], d, n) that rotates arr[] of size n by d elements.

mainList = [1,2,3,4,5,6,7]

def rotate(aList, d, n):
	
	for k in range(0,n):
		# temp = aList[k-d]
		mainList[k] = aList[(k+d)-n]
		# aList[k-1] = aList[k]
		# aList[k] = temp
		print mainList

rotate([1,2,3,4,5,6,7],2,7)

#		0,1,2,3,4,5,6
#		2,3,4,5,6,7,8
#		2,3,4,5,6,0,1
# 0 2 0
# 1 3 1