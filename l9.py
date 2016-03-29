# palindrome number without extra spaces

def isP(n):
	highest = -1
	while (n > 10**highest):
		highest += 1
	for i in range(highest, 0, -2):
		if n // (10**i) != (n % 10):
			return False
		n = n % (10**i) # chop off the first
		n //= 10 # chop off the last
	return True