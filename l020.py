s1 = '(([]){})' # valid
s2 = '{[[]}]' # invalid: interleaved
s3 = '((([' # invalid: left open

match = {'(':')', '[':']', '{':'}'}

def isValid(s):
	stack = []
	for each in s:
		if each == '(' or each == '[' or each == '{':
			stack.append(each)
		elif stack == [] or each != match[stack[-1]]:
			return False
		else:
			stack.pop(-1)
	return True if stack == [] else False