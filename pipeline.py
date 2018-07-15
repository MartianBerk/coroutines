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
	try:
		while True:
			line = (yield)
			if pattern in line:
				print(line)
	except GeneratorExit:
		print("Going away. Goodbye")

file = open('lines.txt')
lines = follow(file)

g = grep("match")

for line in lines:
	g.send(line)

g.throw(RuntimeError, "You're hosed")
g.close()
