pad = {'0':(''), '1':(''), '2':('a','b','c'), '3':('d','e','f'), '4':('g','h','i'), '5':('j','k','l'), 
       '6':('m','n','o'), '7':('p','q','r','s'), '8':('t','u','v'), '9':('w','x','y','z')}

def f(digits):
	ret, new = [''], []
	for i in range(len(digits)):
		new = []
		for each in ret:
			for d in pad[digits[i]]:
				new.append(each+d)
		ret = new
	return new