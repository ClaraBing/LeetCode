# med(m, n) gives the median of the two sorted input array m and n.
def med(m, n):
	l = len(m) + len(n)
	if l % 2 == 0:
		return (get(m, n, l//2) + get(m, n, l//2+1)) / 2
	return get(m, n, l - l//2)

# get(m, n, k): the helper function which returns the kth smallest number in the sorted input array m and n.
def get(m, n, k):
	if k != int(k):
		return -1
	k = int(k)
	if m == []: return n[k-1]
	if n == []: return m[k-1]
	if k == 1:
		return min(m[0], n[0])
	t1, t2 = min(len(m)-1, k // 2 - 1), min(len(n)-1, k // 2 - 1)
	if m[t1] >= n[t2]:
		return get(m, n[t2+1:], k-t2-1)
	return get(m[t1+1:], n, k-t1-1)
