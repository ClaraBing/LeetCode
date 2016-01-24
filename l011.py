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
