# longest common prefix among an array of strings

a = ["abab", "aba", "abc"]
b = ["bade", "ade", "adc"]
c = ["abac", "aba", "abacd"]

def lcp(lst):
	ret, retCnt = lst[0], len(lst[0])
	for each in lst[1:]:
		retCnt = min(retCnt, len(each))
		for j in range(retCnt):
			if ret[j] != each[j]:
				retCnt = j
				break;
	return ret[:retCnt]

class Solution(object):
	def longestCommonPrefix(self, strs):
		ret, retCnt = lst[0], len(lst[0])
		for each in lst[1:]:
			retCnt = min(retCnt, len(each))
			for j in range(retCnt):
				if ret[j] != each[j]:
					retCnt = j
					break;
		return ret[:retCnt]