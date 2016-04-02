# I, V, X, L, C, D, M

# Roman to integer
def r2i(s):
	val = 1000*s.count('M') + 500*s.count('D') + 100*s.count('C') + 50*s.count('L') + 10*s.count('X') + 5*s.count('V') + s.count('I')
	lst = [('M','C',200), ('D','C',200), ('C','X',20), ('L','X',20), ('X','I',2), ('V','I',2)]
	for each in lst:
		pos = s.rfind(each[0])
		if pos != -1 and pos>0 and s[pos-1] == each[1]: val -= each[2]
	return val