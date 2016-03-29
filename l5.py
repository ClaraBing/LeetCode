class Solution(object):
	def longestPalindrome(self, s):
		pre = "^#" + '#'.join(list(s)) + "#$"
		c, r, p = 0, 0, []
		for i, char in enumerate(pre):
			if r > i:
				p.append(min(r-i, p[2*c-i]))
			else:
				p.append(0)
			while i - p[i]-1 >= 0 and (i+p[i]+1) < len(pre) and pre[i-p[i]-1] == pre[i+p[i]+1]:
				p[i] += 1
			if i + p[i] > r:
				c, r = i, i + p[i]
		half = max(p)
		center = p.index(half)
		return ''.join([x for x in pre[center-half:center+half+1] if x != '#'])


# O(n)
def l(s):
	pre = "#" + '#'.join(list(s)) + "#"
	# print(pre)
	c, r = 0, 0
	p = []
	for i, char in enumerate(pre):
		# if r > i:
		# 	p.append(min(r-i, p[2*c-i]))
		# else:
		# 	p.append(0)
		p.append(min(r-i, p[2*c-i])) if r > i else p.append(0)
		while i - p[i]-1 >= 0 and (i+p[i]+1) < len(pre) and pre[i-p[i]-1] == pre[i+p[i]+1]:
			p[i] += 1
		if i + p[i] > r:
			c, r = i, i + p[i]
	half = max(p)
	center = p.index(half)
	return ''.join([x for x in pre[center-half:center+half+1] if x != '#'])

# def pre(s):
# 	return "^" + '#'.join(list(s)) + "#$"

# time limit exceeded

def check(s):
	longest = 0
	# palindrome with odd length
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
	# palindrome with even length
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

# def p(s):
	# l = len(s)
	# ss = [s]
	# rs = s[::-1]
	# rss = [rs]
	# while l > 0:
	# 	ht = {}
	# 	for each in ss:
	# 		ht[hash(each)] = each
	# 	for each in rss:
	# 		if hash(each) in ht:
	# 			return ht[hash(each)]
	# 	nss = [s[:l-1]]
	# 	for each in ss:
	# 		nss.append(each[1:])
	# 	ss = nss
	# 	nrss = [rs[:l-1]]
	# 	for each in rss:
	# 		nrss.append(each[1:])
	# 	rss = nrss
	# 	l -= 1
	# return "No palindrome"