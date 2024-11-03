def mysum(l):
	"""
	input is list
	>>> mysum([1, 2, 3, 4, 5])
	15
	>>> mysum([])
	0
	"""
	if l == []:
		return 0
	else:
		return l[0] + mysum(l[1:])

def sum_recur(n):
	if n == 1:
		return 1
	else:
		return n + sum_recur(n - 1)
	
def sum_iter(n):
	sum = 0
	for x in range(1, n + 1):
		sum += x
	return sum

def reverse_recur(str):
	if len(str) == 1:
		return str
	else:
		return reverse_recur(str[1:]) + str[0]