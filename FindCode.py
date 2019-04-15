def findCode(positions, letters, n):
    l = [None] * n

    for i in range(len(positions)):
        #print(i)
        if positions[i] >= n:
            return ''
        if not l[positions[i]]:
            l[positions[i]] = {letters[i] : 1}
        else:
            if letters[i] in l[positions[i]]:
                l[positions[i]][letters[i]] += 1
            else:
                l[positions[i]][letters[i]] = 1
        #print(l)

    ret = ''
    #print(l)
    for i in range(n):
        if not l[i]:
            return ''

        for key in l[i].keys():
            if l[i][key]/n > 0.5:
                ret += key

    return ret

if __name__ == '__main__':
    print(findCode([1, 0, 0, 0, 2, 2, 2], ['+', 'A', 'C', 'B', '#', '#', '#'], 3))
    print(findCode([1, 3, 3, 3, 2, 2, 2], ['+', 'A', 'C', 'B', '#', '#', '#'], 3))
