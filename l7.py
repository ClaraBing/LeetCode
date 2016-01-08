# Problem 7: Reverse Integer

# 32-bit int boundary
INT_BOUND = 2147483648

def reverse(self, n):
	val = int(str(abs(n))[::-1])
	if n < 0:
		return - val if val <= INT_BOUND else 0
	return val if val < INT_BOUND else 0
