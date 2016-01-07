# O(n)
def longest(s):
	pre = "#" + '#'.join(list(s)) + "#"
		c, r, p = 0, 0, []
		for i, char in enumerate(pre):
			p.append(min(r-i, p[2*c-i])) if r > i else p.append(0)
			while i - p[i]-1 >= 0 and (i+p[i]+1) < len(pre) and pre[i-p[i]-1] == pre[i+p[i]+1]:
				p[i] += 1
			if i + p[i] > r:
				c, r = i, i + p[i]
		# max(p) is the length of the longest palindrome
		return ''.join([x for x in pre[p.index(max(p))-max(p) : p.index(max(p))+max(p)+1] if x != '#'])



# O(n^2)
# 1: comparison based
def check(s):
	longest = 0
	pos = 0
	for i, each in enumerate(s):
		l, r = i-1, i+1
		tmp = 1
		while l >= 0 and r < len(s):
			if s[l] == s[r]:
				tmp += 2
				l -= 1
				r -= 1
			else:
				longest = max(longest, tmp)
				pos = i
				odd = True
				break
	pos = 1
	for i in range(1, len(s)-1):
		l, r = i-1, i
		tmp = 0
		while l >= 0 and r < len(s):
			if s[l] == s[r]:
				tmp += 2
				l -= 1
				r -= 1
			else:
				longest = max(longest, tmp)
				pos = i
				odd = False
				break
	if odd:
		half = (longest - 1)//2
		return s[pos-half:pos+half+1]
	else:
		half = longest // 2
		return s[pos-half, pos+half]

# 2: using hash value
def p(s):
	# hash value
	l = len(s)
	last = myhash(s, l)
	ht = {last:0}
	rs = s[::-1]
	rlast = myhash(rs, l)
	rht = {rlast:0}
	while l > 0:
		# check against ht
		for each in rht:
			if each in ht:
				return rs[rht[each]:rht[each]+l]
		# reconstruct
		last, ht = next(s, ht, l, last)
		#print("ht: "+str(ht.keys()))
		rlast, rht = next(rs, rht, l, rlast)
		#print("rht: "+str(rht.keys()))
		l -= 1
	return "No palindrome"

def next(s, ht, l, last):
	tmp = {}
	for each in ht.keys():
		tmp[(each - ord(s[ht[each]+l-1]) + 96) // 26] = ht[each]
	last = last - (ord(s[-l]) - 96) * (26 ** (l-1))
	tmp[last] = len(ht)
	return last, tmp

def myhash(s, n):
	val = 0
	for i in range(n):
		val += (ord(s[i]) - 96) * (26 ** (n-1-i))
	return val
