# I, V, X, L, C, D, M

# integer to Roman
def i2r(num):
	m = num // 1000
	num %= 1000
	preM = 0
	if num // 100 == 9:
		preM = 1
		num -= 900
	d = num // 500
	num %= 500
	preD = 0
	c = 0
	if num // 100 == 4:
		preD = 1
	else:
		c = num // 100
	num %= 100
	preC = 0
	if num // 10 == 9:
		preC = 1
		num -= 90
	l = num // 50
	preL = 0
	num %= 50
	x = 0
	if num // 10 == 4:
		preL = 1
	else:
		x = num // 10
	num %= 10
	preX = 0
	if num == 9:
		preX = 1
		num -= 9
	v = num // 5
	num %= 5
	preV = 0
	i = 0
	if num == 4:
		preV = 1
	else:
		i = num
	return m*'M' + preM*'CM' + d*'D' + preD*'CD' + c*'C' + preC*'XC' + l*'L' + preL*'XL' + x*'X' + preX*'IX' + v*'V' + preV*'IV' + i*'I'     