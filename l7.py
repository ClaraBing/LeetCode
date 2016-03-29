# 32-bit int boundary
INT_BOUND = 2147483648

class Solution(object):
	def reverse(self, n):
		val = int(str(abs(n))[::-1])
		if n < 0:
			return - val if val <= INT_BOUND else 0
		return val if val < INT_BOUND else 0

class Solution(object):
	def reverse(self, n):
		if n < 0:
			return - int(str(-n)[::-1]) if int(str(-n)[::-1]) <= INT_BOUND else 0
		return int(str(n)[::-1]) if int(str(n)[::-1]) < INT_BOUND else 0

# 56ms
class Solution(object):
	def reverse(self, n):
		tmp = str(n)
		if tmp[0] == '-':
			return - int(tmp[-1:0:-1]) if int(tmp[-1:0:-1]) <= INT_BOUND else 0
		return int(tmp[::-1]) if int(tmp[::-1]) < INT_BOUND else 0