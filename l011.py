# container with most water
# i.e. max( abs(i-j) * min(ai, aj) )

a = [3, 1, 2, 5, 6] # 12
b = [1, 2, 3, 4, 5] # 6
c = [1, 5, 2, 4, 3] # 9

# O(n)
def linear(lst):
	i, j = 0, len(lst)-1
	curr = 0
	while i < j:
		curr = max(min(lst[i], lst[j]) * (j-i), curr)
		if lst[i] < lst[j]:
			i += 1
		else:
			j -= 1
	return curr

# O(log n)
def log(lst):
	tlst = [(lst[pos], pos) for pos in range(len(lst))]
	d = OrderedDict()
	for i, val in enumerate(lst):
		d[i] = val
	ascend = msort(tlst)
	curr = 0
	for t in ascend:
		items = list(d.items())
		if 2*t[1] < items[0][0] + items[-1][0]:
			curr = max(t[0]*(items[-1][0] - t[1]), curr)
		else:
			curr = max(t[0]*(t[1] - items[0][0]), curr)
		d.pop(t[1], None)
	return curr

def msort(tlst):
	if len(tlst) <= 1:
		return tlst
	mid = len(tlst)//2
	fst, snd = msort(tlst[0:mid]), msort(tlst[mid:])
	i, j = 0, 0
	out = []
	while i < len(fst) and j < len(snd):
		if fst[i][0] < snd[j][0]:
			out.append(fst[i])
			i += 1
		else:
			out.append(snd[j])
			j += 1
	if i < len(fst):
		out.extend(fst[i:])
	else:
		out.extend(snd[j:])
	return out

# O(n^2)
def square(lst):
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
# def a(height):
# 	t = {} # table as memory
# 	def h(l, r):
# 		if (l, r) in t:
# 			return t[(l,r)]
# 		if l >= r:
# 			return 0
# 		t[(l, r)] = max(min(lst[l], lst[r]) * (r - l), h(l+1, r), h(l, r-1))
# 		return t[(l,r)]
# 	return h(0, len(lst)-1)

# t = {} # table as memory
# class Solution(object):
# 	def maxArea(self, height):
# 		"""
# 		:type height: List[int]
# 		:rtype: int
# 		"""
# 		t = {} # table as memory
# 		def h(l, r):
# 			if (l, r) in t:
# 				return t[(l,r)]
# 			if l >= r:
# 				return 0
# 			t[(l, r)] = max(min(lst[l], lst[r]) * (r - l), h(l+1, r), h(l, r-1))
# 			return t[(l,r)]
# 		return h(0, len(lst)-1)

# brute force: O(n^2)
# def bf(bars):
# 	currM = 0
# 	for i in range(len(bars)):
# 		cnt = 0
# 		for j in range(1, len(bars)-i):
# 			if bars[i+j] >= bars[i]:
# 				cnt = j
# 			else:
# 				currM = max(currM, j*bars[i+j])
# 		currM = max(currM, cnt*bars[i])
# 	return currM