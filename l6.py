s = "PAYPALISHIRING"

def zigZag(s, n):
	if n == 1:
		return s
	s = list(s)
	diff = 2*n - 2 - len(s)%(2*n-2)
	# append '' to s to make len(s) to be the multiple of (2*n - 2)
	s.extend(['' for _ in range(diff)])
	rows = [[] for _ in range(n)]
	for i in range(0, len(s)//(2*n-2)):
		base = i*(2*n-2) + n - 1
		rows[0].append(s[base-n+1])
		for j in range(n-2, 0, -1):
			rows[n-1-j] += [s[base-j],s[base+j]]
		rows[n-1].append(s[base])
	return ''.join([''.join(row) for row in rows])

class Solution(object):
	def convert(self, s, n):
		"""
		:type s: str
		:type numRows: int
		:rtype: str
		"""
		if s == "" or n == 1:
			return s
		curr, sign = 0, False
		rows = [[] for _ in range(n)]
		rows[0] = [s[0]]
		for each in s[1:]:
			if curr == n-1 or curr == 0:
				sign = not sign
			curr += 1 if sign else -1
			rows[curr].append(each)
		return ''.join([''.join(row) for row in rows])