def pow(x, y):
	sum, k = 1, 0
	while k < y:
		sum, k = sum * x, k + 1
	
	return sum


def curried_pow(x):
	def h(y):
		return pow(x, y)
	return h

def map_to_range(start, end, f):
	while start < end:
		print(f(start))
		start += 1
