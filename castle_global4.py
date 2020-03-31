import math

N = int(raw_input())

mainList = []
for x in range(0,N):
	mainList.append(int(raw_input()))


for k in mainList:
	if k % 2 == 0: # square
		pieces = (k / 2 )*(k / 2)
	else : # rectangle
		edge1 = math.floor(k/2)
		edge2 = k - edge1
		pieces = edge1 * edge2
	print int(pieces)
