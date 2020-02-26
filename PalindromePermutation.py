'''
Given a string, write a function to check if it is a permutation of a palindrome.

'''

def isPalinPerm(s):
    a = [False] * 26

    for c in s:
        if c != ' ':
            a[ord(c) - ord('a')] = not a[ord(c) - ord('a')]
    
    count  = 0
    for i in a:
        if i:
            count += 1

    return count <= 1  

a = 'taco cat'
print(isPalinPerm(a))
a = 'abc de'
print(isPalinPerm(a))
a = 'ascdedcsa'
print(isPalinPerm(a))