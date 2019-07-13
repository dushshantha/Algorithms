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
    
l = ['zero', 'one', 'two', 'three', 'four','five']
def convert(name):
    return l.index(name)


print(sortByName(['alex one', 'test3 five', 'test1 two']))
print(sortByName(['test1 two', 'alex five', 'alex two']))
print(sortByName(['alex one', 'test1 five', 'test1 two']))
print(sortByName(['alex one', 'test1 five', 'test1 two', 'test1 two']))