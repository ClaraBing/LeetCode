# Problem 8: atoi

INT_MAX = 2147483647
INT_MIN = -2147483648

def myAtoi(s):
	s = s.strip()
	res, neg = 0, False
	if s != "" and (s[0] == '-' or s[0] == '+'):
		if s[0] == '-':
			neg = True
		s = s[1:]
	if s == "":
		return 0
	for char in s:
		if not char.isdigit():
			break
		res = res * 10 + ord(char) - 48
	if neg:
		res = - res
	if res < INT_MIN:
		return INT_MIN
	if res > INT_MAX:
		return INT_MAX
	return res
