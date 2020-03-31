"""
given a sequence determine if AP or GP
and return next number
"""


def isAP(lst):
	if len(lst) > 1:
		# try to calculate diff by using first two elements
		diff = lst[1] - lst[0]
		# now try to see if diff fits
		for i in range(len(lst) - 1):
			if (lst[i] + diff) != lst[i+1]:
				return 0
		return diff
	else:
		return 0

def isGP(lst):
	if len(lst) > 1:
		# try to calculate ratio by using first two elements
		ratio = lst[1] / lst[0]
		# now try to see if ratio fits
		for i in range(len(lst) - 1):
			if (lst[i] * ratio) != lst[i+1]:
				return 0
		return int(ratio)
	else:
		return 0


input_seq = input()

input_lst = [int(_) for _ in input_seq.split(' ')]

isAP = isAP(input_lst)
isGP = isGP(input_lst)

if isAP > 0:
	print('AP_{0}'.format(isAP))
elif isGP > 0:
	print('GP_{0}'.format(isAP))