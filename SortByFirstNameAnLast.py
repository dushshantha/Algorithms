'''
Sort a list of first name last name strings by first name alphabatically. If there are more same first names, sort by the numerical value of last name

example:
[alex one, test3 five, test1 two] => [alex one, test1 two, test3 five]
[test1 two, alex five, alex two] => [alex two, alex five, test1 two]
'''
from functools import cmp_to_key

def sortByName(names):
    print(names)
    names.sort(key=cmp_to_key(lambda x, y: 1 if convert(x.split(' ')[-1]) > convert(y.split(' ')[-1]) and  x > y else -1))
    return names

def sortArrays(a):
    print(a)
    a.sort(key=cmp_to_key(lambda x, y: 1 if x[0] >= y[0] else -1))
    return a

def intervalMerge(a):
    a = sortArrays(a)
    stack = [a[0]]

    for i in range(1, len(a)):
        if a[i][0] >= stack[0][0] and a[i][0] <= stack[0][1]: # Is overlap
            stack[0] = [min(a[i][0], stack[0][0]), max(a[i][1], stack[0][1])]
        else:
            stack.insert(0, a[i])
    return stack[::-1]

l = ['zero', 'one', 'two', 'three', 'four','five']
def convert(name):
    return l.index(name)


print(sortByName(['alex one', 'test3 five', 'test1 two']))
print(sortByName(['test1 two', 'alex five', 'alex two']))
print(sortByName(['alex one', 'test1 five', 'test1 two']))
print(sortByName(['alex one', 'test1 five', 'test1 two', 'test1 two']))

print(sortArrays([[3,5], [1,3],[7,9], [5,8],[2,5]]))

print(intervalMerge([[3,5], [1,3],[7,9], [5,8],[2,5]]))
print(intervalMerge([[3,5], [1,3],[7,9], [5,8],[2,5],[10,12]]))