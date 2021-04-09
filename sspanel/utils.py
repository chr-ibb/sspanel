# TODO header

def get_between(s: str, before: str, after: str):
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