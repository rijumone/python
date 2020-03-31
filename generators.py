print "========== gencubes(10) =========="

def gencubes(n):
	for num in range(n):
		yield num**3


for x in gencubes(10):
	print x

print "========== genfibon(10) =========="

def genfibon(n):
	a = 0
	b = 1

	for i in range(n):
		# c = a
		# a = b
		# b = a + c
		# yield b
		yield a
		a,b = b, a+b


for x in genfibon(10):
	print x


# f = genfibon(1000)

# print next(f)
# print next(f)
# print next(f)
# print next(f)