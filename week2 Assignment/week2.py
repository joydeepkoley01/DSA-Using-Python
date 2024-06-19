def threesquares(m):
	if(m<0):
		return False
    while m%4==0:
		m/=4
	if m%8==7:
		return False
	else:
		return True
def repfree(s):
	seen_chars = set()
	for char in s:
		if char in seen_chars:
			return False
		seen_chars.add(char)
	return True
