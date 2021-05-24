'''
https://leetcode.com/discuss/interview-question/912928/AMAZON-or-OA-2020-or-GIFTING-GROUPS-or-FRIEND-CIRCLE-LC-DOESNT-SOLVE-THIS

'''

def countGroups(related):
    count = 0
    n = len(related)
    for i in range(n):
        print(related)
        if related[i] != True:
            count += 1
            countHelper(related, related[i], n)
    return count

def countHelper(related, s, n):
    for j in range(n):
        if related[j] != True and s[j] == '1':
            m = related[j] 
            related[j] = True
            countHelper(related, m, n)
    

print(countGroups(['1100', '1110', '0110', '0001']))
print(countGroups(['11100', '11001', '10100', '00011', '01011']))
print(countGroups(['11100', '11100', '11100', '00011', '00011']))
print(countGroups(['10100', '01010', '10100', '01010', '00001']))



