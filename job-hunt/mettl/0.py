"""
find smallest palindromic integer greater than 'n'
"""

import math

def isP(n):
	n_str = str(n)
	for i in range(0, math.floor((len(n_str)/2))):
		if n_str[i] != n_str[len(n_str) - 1 - i]:
			return False
	return True


n = int(input())

while True:
	if isP(n):
		print(n)
		break
	else:
		n += 1