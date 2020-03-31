import math
import string

def vol(rad):
	print ((4 * math.pi * rad ** 3)/3) 

vol(5)

print "======================================="

def ran_bool(num, low, high):

	for k in range(low,high+1):
		if num == k:
			return True

	return False

print ran_bool(101, 5, 100)

print "======================================="
# print string.ascii_lowercase
# print string.ascii_uppercase

def up_low(s):
	nU = 0
	nL = 0
	for k in s:
		if k in string.ascii_lowercase:
			nL = nL + 1
		if k in string.ascii_uppercase:
			nU = nU + 1

	print nU
	print nL

up_low("H h I")

print "======================================="

lCntDict = {}

for k in string.ascii_lowercase:
	lCntDict[k] = 0



def isPanagram(s):
	s = s.replace(" ","")
	for k in s:
		k = k.lower()
		lCntDict[k] = lCntDict[k] + 1
	for k in lCntDict:
		if lCntDict[k] == 0:
			return False
	return True
		

print isPanagram("the quick brown fox jumps over the lazy dog")		

print "======================================="

