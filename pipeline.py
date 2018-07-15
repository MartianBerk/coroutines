import time

def follow(file):
	while True:
		line = file.readline()
		if not line:
			break

		yield line

def coroutine(func):
	def start(*args, **kwargs):
		cr = func(*args, **kwargs)
		cr.next()
		return cr
	return start

@coroutine
def grep(pattern):
	print('looking for %s' % pattern)
	while True:
		line = (yield)
		if pattern in line:
			print(line)

file = open('lines.txt')
lines = follow(file)

g = grep("match")

for line in lines:
	g.send(line)

g.close()
