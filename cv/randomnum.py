import itertools as it

c = it.cycle(range(6))

def getRandomNum () :
	for x in range(100):
		return next(c)