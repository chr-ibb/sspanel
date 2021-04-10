# TODO header
# TODO am I using search_between? should I switch them around? 

def search_between(s: str, before: str, after: str):
	"""Searches a string and finds the first substring found between the
	before and after substrings, if they are found.
	Returns the substring and the index it was found at.

	example:
	>>> get_between("hayneedlestack", "hay", "stack")
	('needle', 3)

	>>> get_between("hello world", "hay", "stack")
	("", 0)
	"""
	start = s.find(before) + len(before)
	if start < 0: return "", 0

	end = s[start:].find(after)
	if end < 0: return "", 0

	return s[start:start+end], start + end


def get_between(s: str, before: str, after: str):
	"""Same as search_between, but only returns the resulting string"""
	return search_between(s, before, after)[0]


def multi_find(s: str, f: str):
	"""finds every occurance of f in s"""
	res = []
	scanned = 0
	while len(s) > 0:
		found = s.find(f)
		if found == -1: break

		res.append(found + scanned)
		s = s[found + 1:]
		scanned += found + 1
	return res