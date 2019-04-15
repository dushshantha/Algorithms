# abcXdef  abcYYdef = X,YY
# abcd abc = d , ''
# abcd abdd = c, d
# aa, a = a, ''

def findTheChange(old, new):
    start = 0
    i = 0

    len_old = len(old) 
    len_new = len(new) 

    while i < len_new and i < len_old and old[i] == new[i]:
        i += 1

    start= i

    a , b = len_old - 1, len_new - 1

    while start <= a and start <= b and old[a] == new[b]:
        a -= 1
        b -= 1
    
    return start, old[start:a + 1], new[start:b + 1]

if __name__ == "__main__":
    print(findTheChange('abcXdef', 'abcYYdef'))
    print(findTheChange('abcd', 'abc'))
    print(findTheChange('abcd', 'abdd'))
    print(findTheChange('aa', 'a'))
    print(findTheChange('aca', 'acca'))
    



