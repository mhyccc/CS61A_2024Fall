def race(x, y):
	"""The tortoise always walks x feet per minute, while the hare repeatedly
	runs y feet per minute for 5 minutes, then rests for 5 minutes. Return how
	many minutes pass until the tortoise first catches up to the hare.
	>>> race(5, 7) # After 7 minutes, both have gone 35 steps
	7
	>>> race(2, 4) # After 10 minutes, both have gone 20 steps
	10
	>>> race(2, 3) # wrong answer
	8
	"""
	assert y > x and y <= 2 * x, 'the hare must be fast but not too fast'
	tortoise, hare, minutes = 0, 0, 0
	while minutes == 0 or tortoise - hare < 0:
		tortoise += x
		if minutes % 10 < 5:
			hare += y
		minutes += 1
	return minutes

def fizzbuzz(n):
	"""
	>>> result = fizzbuzz(16)
	1
	2
	fizz
	4
	buzz
	fizz
	7
	8
	fizz
	buzz
	11
	fizz
	13
	14
	fizzbuzz
	16
	>>> print(result)
	None
	"""
	k = 1
	while k <= n:
		if k % 3 == 0 and k % 5 == 0:
			print("fizzbuzz")
		elif k % 3 == 0:
			print("fizz")
		elif k % 5 == 0:
			print("buzz")
		else:
			print(k)
		k += 1

def isPrime(n):
	"""
	>>> isPrime(13)
	True
	>>> isPrime(14)
	False
	>>> isPrime(1)
	False
	>>> isPrime(2)
	True
	>>> isPrime(3)
	True
	
	"""
	if n == 1:
		return False
	
	k = 2
	while k < n:
		if n % k == 0:
			return False
		k += 1
	return True

def unique_digits(n):
	"""Return the number of unique digits in positive integer n.
	>>> unique_digits(8675309) 	# All are unique
	7
	>>> unique_digits(13173131) # 1, 3, and 7
	3
	>>> unique_digits(101) 		# 0 and 1
	2
	>>> unique_digits(1211011)  # 0, 1 and 2
	3
	"""
	ans = 0
	while n > 0:
		last = n % 10
		n //= 10
		if not has_digit(n, last):
			ans += 1
	return ans

def has_digit(n, k):
	"""Returns whether k is a digit in n.
	>>> has_digit(10, 1)
	True
	>>> has_digit(12, 7)
	False
	>>> has_digit(12, 2)
	True
	"""
	while n > 0:
		if n % 10 == k:
			return True
		n //= 10
	return False