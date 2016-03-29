# Problem 6: ZigZag Conversion

def convert(s, n):
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
