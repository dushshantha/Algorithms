'''
There are three type of edits. Insert, delete or replace. Given 2 strings , find out if the 2 are just one edit (or 0) away.
pale -> ple  = True
pale -> bale = True
pales -> pale = True
pale -> bake = False
'''

def isOneAway(s1, s2):
    if len(s1) == len(s2): # replace
        return isOneReplaceAway(s1,s2)
    elif len(s1) > len(s2): # delete
        return isAddition(s2, s1)
    else:
        return isAddition(s1, s2)

def isOneReplaceAway(s1,s2):
    replaced = False

    for i in range(len(s1)):
        if s1[i] != s2[i]:
            if replaced:
                return False
            replaced = True
    
    return True

def isAddition(s1, s2):
    i, j = 0, 0
    while j > len(s2):
        if s1[i] != s2[j]:
            j += 1
        else:
            j += 1
            i += 1
        
    return j - 1 <= 1 

print(isOneAway('pale', 'ple')) # Delete
print(isOneAway('pale', 'bale')) #Replace
print(isOneAway('pale', 'pales')) # insert
print(isOneAway('pale', 'bake')) # No way
