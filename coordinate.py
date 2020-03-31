class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self):
        return "Coord: " + str(self.__dict__)
def add(a, b):
	# print Coordinate(a.x + b.x, a.y + b.y)
	return Coordinate(a.x + b.x, a.y + b.y)
def sub(a, b):
    return Coordinate(a.x - b.x, a.y - b.y)
one = Coordinate(100, 200)
two = Coordinate(300, 200)
print add(one, two)

# class Foo:
# 	def __init__(self):
# 		print "hn ho gya object call"
# 	def __repr__(self):
# 		return "hn bhai ek __repr__ method override krke bhi dal dia is bar"

# print Foo	# class print krna
# print Foo()	# class ko instantiate krna
# ekorvar = Foo()	# sirf __init__ k print ayga
# print ekorvar	# ab __repr__ k print b ayga


def makebold(fn):
    def wrapped():
        return "<b>" + fn() + "</b>"
    return wrapped

def makeitalic(fn):
    def wrapped():
        return "<i>" + fn() + "</i>"
    return wrapped

# @makebold
# @makeitalic
def hello():
    return "hello world"


hello = makeitalic(hello)
hello = makebold(hello)

print hello() ## returns "<b><i>hello world</i></b>"