# UF.py

class UF:
	
	N = 0
	p, q = None, None
	
	def __init__(self, N):
		self.N = N

	def union(self, p, q):
		pass

	def connected(self, p, q):
		return False


if __name__ == '__main__':
	with open('tinyUF.txt') as input_file:
		first = True
		for line in input_file:
			if first:
				UF(line.strip('/n'))			
			first = False
			UF.p(line.strip('\n').split(' ')[0])
			UF.q(line.strip('\n').split(' ')[1])
