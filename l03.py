class Solution(object):
    def lengthOfLongestSubstring(self, strg):
    	"""
    	:type strg: str
    	:rtype: int
    	"""
    	table = {}
    	accum = 0
    	currMax = 0
    	start = 0
    	for pos, i in enumerate(strg):
    		if i not in table:
    			table[i] = pos
    			accum += 1
    		else:
    			currMax = max(currMax, accum)
    			if table[i] >= start:
    				accum = pos - table[i]
    				start = table[i] + 1
    			else:
    				accum += 1
    			table[i] = pos
    	return max(currMax, accum)
