# Porblem: https://leetcode.com/problems/two-sum/

def twoSum(lst, tar):
	dct = {}
	for i, val in enumerate(lst):
		if tar-val in dct:
			print ("index1=" + str(dct[tar-val]+1) + ", index2=" + str(i+1))
			return
		dct[val] = i
	print "Not Found"
