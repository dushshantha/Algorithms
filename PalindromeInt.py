'''
Given an integer, check if that integer is a palindrome. For this problem do not convert the integer to a string to check if it is a palindrome.
'''
def palindromeInt(n):
    orig = n
    rev = 0

    while orig > 0:
        rev = (rev * 10) + orig % 10
        orig = orig // 10
    
    return n == rev


print(palindromeInt(12321))
print(palindromeInt(12322))
print(palindromeInt(0))
print(palindromeInt(1111))