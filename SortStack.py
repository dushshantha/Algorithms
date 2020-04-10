'''
Sort values in a stack. You can use an temp stack if you like
'''

def push(s, x):
    s.append(x)

def pop(s):
    if s:
        return s.pop(-1)
    return None

def peek(s):
    return s[-1]

def isEmpty(s):
    return True if s else False

def sort(s):
    if not s:
        return s

    s_tmp = []
    v = pop(s)
    push(s_tmp, v)

    while s:
        v = pop(s)
        if peek(s_tmp) <= v:
            push(s_tmp, v)
        else:
            while s_tmp and peek(s_tmp) > v:
                push(s, pop(s_tmp))
            push(s_tmp,v)
    
    while s_tmp:
        push(s, pop(s_tmp))

    


stack = [1,2,3,4,5]
push(stack, 6)
print(stack)
print(pop(stack))
print(stack)
sort(stack)
print(stack)
print('----------')
stack = [1,1,1,1,1]
print(stack)
sort(stack)
print(stack)
print('----------')
stack = [1]
print(stack)
sort(stack)
print(stack)

print('----------')
stack = []
print(stack)
sort(stack)
print(stack)