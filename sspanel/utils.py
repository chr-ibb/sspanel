# TODO header

def find_between(s: str, before: str, after: str):
	"""Searches string S and finds the first substring found between the
	BEFORE and AFTER substrings, if they are found.
	
	Returns the indexes of the start and end of the found substring,
	such that s[start:end] would be the substring. (first character, last character + 1)

	If not found, (0,0) is returned. 

	example:
	>>> find_between("hayneedlestack", "hay", "stack")
	(3, 9)

	>>> find_between("hello world", "hay", "stack")
	(0, 0)
	"""
	start = s.find(before) + len(before)
	if start < 0: return 0, 0

	end = s[start:].find(after)
	if end < 0: return 0, 0

	return start, start + end


def string_between(s: str, before: str, after: str):
	"""Returns the substring of S that is between the first occurrence of 
	BEFORE and the next occurrence of AFTER, if it is found.

	example:
	>>> string_between("hayneedlestack", "hay", "stack")
	"needle"

	>>> string_between("haystack", "hay", "stack")
	""

	>>> string_between("hello world", "hay", "stack")
	None

	"""
	indexes = find_between(s, before, after)
	if indexes == (0, 0): return None
	return s[indexes[0]:indexes[1]]


def multi_find(s: str, f: str):
	"""Finds every occurrence of substring F in string S.
	Returns a list of indexes where each occurence starts."""
	res = []
	scanned = 0
	while len(s) > 0:
		found = s.find(f)
		if found == -1: break

		res.append(found + scanned)
		s = s[found + 1:]
		scanned += found + 1
	return res