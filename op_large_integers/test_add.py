from random import randrange
from op_large_integers import add

def test_add():
	for _ in range(999):
		a = randrange(1, 100)
		b = randrange(1, 100)
		assert str(a + b) == add(a, b)


# def get_seas


if __name__ == '__main__':
	print(add(19, 31))