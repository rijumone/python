#!/usr/local/bin/python3
import math



def halve(lst):
	'''
	input lst
	output lst0, lst1
	'''

	if len(lst) == 1:
		print(lst[0])
	else:
		halve(lst[:math.floor(len(lst)//2)])
		halve(lst[math.floor(len(lst)//2):])

		
if __name__ == '__main__':
	print('input list elements as space separated integes')
	lst = [int(_) for _ in input().split(' ')]
	halve(lst)