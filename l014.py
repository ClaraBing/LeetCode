# longest common prefix among an array of strings

def lcp(lst):
	if lst == []: return ""
	comm = lst[0]
	for each in lst[1:]:
		comm = comm[: min(len(each), len(comm))]
		for i in range(len(comm)):
			if comm[i] != each[i]:
				comm = comm[:i]
				break
	return comm