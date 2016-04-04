def f(n):
	if n == 0:
		return ['']
	return h([''], 0, n)

def h(s, opening, remain):
	sub1 = []
	for each in s:
		sub1.append(each+')')
	if remain == 0:
		ret = []
		for each in sub1:
			ret.append(each+(opening-1)*')')
		return ret
	sub2 = []
	for each in s:
		sub2.append(each+'(')
	if opening == 0:
		return h(sub2, 1, remain-1)
	return h(sub1, opening-1, remain) + h(sub2,opening+1, remain-1)