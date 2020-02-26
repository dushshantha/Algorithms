def isPerm(s1, s2):
    if len(s1) != len(s2):
        return False
    s1, s2 = sorted(s1), sorted(s2)
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            return False
    return True


print(isPerm('abc', 'acb') == True)
print(isPerm('abc', 'abc') == True)
print(isPerm('aabbccdd', 'aabbccdd') == True)
print(isPerm('', 'acb') == False)
print(isPerm('abdcs', 'aghstud') == False)
print(isPerm('ab', 'acb') == False)