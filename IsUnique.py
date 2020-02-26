def isUnique(s): # O(n) time O(1) space becoz its always 256
    d = [False] * 256
    for c in s:
        if d[ord(c)]:
            return False
        d[ord(c)] = True
    return True

def isUnique_NoSpace(s): # O(n^2)
    for i in range(len(s) - 1):
        if s[i] in s[i + 1:]: 
            return False
    return True


print(isUnique('abcde') == isUnique_NoSpace('abcde'))
print(isUnique('') == isUnique_NoSpace(''))
print(isUnique('abcdec') == isUnique_NoSpace('abcdec'))
print(isUnique('abcdec') == isUnique_NoSpace('abcdec'))
