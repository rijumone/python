import sys
from loguru import logger

logger.add("/tmp/op_large_integers.log")

def main():
	if sys.argv[1] == 'add':
		return add(sys.argv[2], sys.argv[3], )


def add(a, b):
	a = str(a)
	b = str(b)
	logger.info(a + ' + ' + b)
	result = ''
	# reverse the strings to make calculations easier
	rev_a = a[len(a)::-1]
	rev_b = b[len(b)::-1]
	
	# start adding the digits from the end
	max_len = max(len(a), len(b))
	t_c = 0 # to hold carry over if any
	for digit_place in range(max_len):
		t_a = int(rev_a[digit_place]) if len(rev_a) > digit_place else 0
		t_b = int(rev_b[digit_place]) if len(rev_b) > digit_place else 0
		_tmp = t_a + t_b + t_c
		if _tmp > 9:
			# there will be a carry over
			# save the carry over part to t_c
			t_c = 1 # can't be greater than 1 since we are adding at most 2 digits
			_tmp = str(_tmp)[-1] # get only the last digit from _tmp
		else:
			t_c = 0

		result += str(_tmp)
	# print('t_c', t_c)
	append_this = str(t_c) if t_c > 0 else ''
	f_result = append_this + result[len(result)::-1]
	logger.info(f_result)
	return f_result


if __name__ == '__main__':
	print(main())