def repfree(s):
    seen_chars = set()
    for char in s:
        if char in seen_chars:
            return False
        seen_chars.add(char)
    return True
def threesquares(n):
    if(n<0):
        return False
    while n%4==0:
        n//=4
    print(n)
    if n%8==7:
        return False
    else:
        return True