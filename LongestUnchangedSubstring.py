'''
2 string lists
['123', '456','789','123', '456','789'] and ['123', '458','789','123', '456','789']

return [4,2] meaning length of the unchanged substring is 4 and 2 as the starting index
'''

def findUnchanged(l1,l2):
    ret = [0,0]
    s = 0
    while s < len(l1):
        e = s
        print(e)
        while e < len(l1) and l1[e] == l2[e] :
             e += 1
        
        if ret[0] < e - s:
            ret = [e-s, s]
        
        s = e + 1
    return ret

if __name__ == "__main__":
    print(findUnchanged(['123', '456','789','123', '456','789'],['123', '458','789','123', '456','789']))
    print(findUnchanged(['123', '456','789','123', '456','789'],['123', '456','789','123', '457','789']))
    print(findUnchanged(['123', '456'],['789','123']))
    print(findUnchanged(['123', '456'],['123','789']))