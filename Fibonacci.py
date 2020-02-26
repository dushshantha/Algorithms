import random

def fib(i):
    memo = {0: 0,
            1: 1}
    return fibHelper(i, memo)

# Recursion with Dynamic Programming
def fibHelper(i, memo):
    if i in memo:
        return memo[i]
    memo[i] = fibHelper(i - 1, memo) + fibHelper(i - 2, memo)
    return memo[i]

# Non recursive better performance in Space Complexity
def fib2(i):
    if i in (0,1):
        return i
    prev, prev_1 = 0,1
    for j in range(2, i + 1):
        n = prev + prev_1
        prev = prev_1
        prev_1 = n

    return prev_1

def fib3(n):
    l = [0,1]
    if n > 1:
        for i in range(2, n + 1):
            l.append(l[-1] + l[-2])
    return l[n]


if __name__ == '__main__':
    
    '''
    while True:
        n = random.randint(0, 100)
        if fib2(n) != fib3(n):
            print("FAILED at ", n)
            break
        else:
            print("OK")
    '''
    
    print(fib3(0))
    print(fib3(1))
    print(fib3(2))
    print(fib3(3))
    print(fib3(4))
    print(fib3(5))
    print(fib3(6))
