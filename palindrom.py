def palindrom(s):
    for i in range(len(s)//2):
        if s[i] != s[len(s)-1 - i]:
            return False
    return True


if __name__ == "__main__":
    s1 = 'abcdcba' # True
    s2 = 'wewerewrw' # False
    s3 = '' # True

    print(palindrom(s1))
    print(palindrom(s2))
    print(palindrom(s3))