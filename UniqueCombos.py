
# s = ['a','b','c']
def permute(s):

    def permute_helper(s, i, l):
        if i == l: # Meet the lenth
            print(''.join(s))
        else:
            for j in range(i, l):
                s[i], s[j] = s[j], s[i]
                permute_helper(s, i + 1, l)
                s[j], s[i] = s[i], s[j]

    permute_helper(s, 0, len(s))

if __name__ == '__main__':
    s = ['A','B','C']
    permute(s)
