# Container with Most Water

def maxArea(self, lst):
	"""
	:type height: List[int]
	:rtype: int
	"""
	l, r = 0, len(lst)-1
	pair, val = (l, r), min(lst[l], lst[r]) * (r-l)
	while l<r:
		if lst[l] < lst[r]:
			l += 1
		else:
			r -= 1
		if min(lst[l], lst[r]) * (r-l) > val:
			pair, val = (l, r), min(lst[l], lst[r]) * (r-l)
	return val

# time limit exceeded
def a(lst):
	t = {}
	def h(l, r):
		if (l, r) in t:
			return t[(l,r)]
		if l >= r:
			return 0
		t[(l, r)] = max(min(lst[l], lst[r]) * (r - l), h(l+1, r), h(l, r-1))
		return t[(l,r)]
	return h(0, len(lst)-1)
