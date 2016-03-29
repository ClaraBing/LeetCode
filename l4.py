l1 = [1,2,3,4,6,10]
l2 = [5,8,9]
l5 = [5,7,8,9]
l3 = [1,2,3]
l4 = [4,5,6,7]

def mid(m, n):
	print(m)
	print(n)
	if m == []:
		return n[0]
	if n == []:
		return m[0]
	if len(m) == 1 and len(n) == 1:
		return (m[0]+n[0])/2
	mm = m[len(m)//2]
	nm = n[len(n)//2]
	print("m1: "+str(mm)+"    m2: "+str(nm))
	if mm == nm:
		return mm
	elif mm < nm:
		mid(m[len(m)//2:], n[:len(n)//2])
	else:
		mid(m[:len(m)//2], n[len(n)//2:])

from math import ceil

def med(m, n):
	# l = len(m) + len(n)
	# if l % 2 == 0:
	# 	return (get(m, n, l//2) + get(m, n, l//2+1)) / 2
	# else:
	# 	return get(m, n, ceil(l/2))
	l = len(m) + len(n)
	if l % 2 == 0:
		return (get(m, n, l//2) + get(m, n, l//2+1)) / 2
	else:
		return get(m, n, l - l//2)

# from math import ceil

def get(m, n, k):
	if k != int(k):
		return -1
	k = int(k)
	if m == []: return n[k-1]
	if n == []: return m[k-1]
	if k == 1:
		return min(m[0], n[0])
	#print("m: "+str(m))
	#print("n: "+str(n))
	t1, t2 = min(len(m)-1, k // 2 - 1), min(len(n)-1, k // 2 - 1)
	if m[t1] >= n[t2]:
		return get(m, n[t2+1:], k-t2-1)
	else:
		return get(m[t1+1:], n, k-t1-1)

class Solution(object):
	def f(self, m, n):
		l = len(m) + len(n)
		if l % 2 == 0:
			return (get(m, n, l//2) + get(m, n, l//2+1)) / 2
		else:
			return get(m, n, 1 + l//2)

# class Solution(object):
# 	def f(self, m, n):
# 		"""
# 		:type nums1: List[int]
# 		:type nums2: List[int]
# 		:rtype: float
# 		"""
# 		l = len(m) + len(n)
# 		if l % 2 == 0:
# 			return (get(m, n, l//2) + get(m, n, l//2+1)) / 2
# 		else:
# 			return get(m, n, ceil(l/2))


# def get(m, n, k):
# 	# print("k: "+str(k))
# 	if m == []: return n[k-1]
# 	if n == []: return m[k-1]
# 	if k == 1:
# 		return min(m[0], n[0])
# 	#print("m: "+str(m))
# 	#print("n: "+str(n))
# 	t1, t2 = min(len(m)-1, k // 2 - 1), min(len(n)-1, k // 2 - 1)
# 	if m[t1] >= n[t2]:
# 		return get(m, n[t2+1:], k-t2-1)
# 	else:
# 		return get(m[t1+1:], n, k-t1-1)


	# if (len(m) + len(n)) % 2 == 0:
	# 	return help(m, n, ((len(m) + len(n)) // 2))
	# else:
	# 	ret