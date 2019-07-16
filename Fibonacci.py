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

if __name__ == '__main__':
    print(fib2(0))
    print(fib2(1))
    print(fib2(2))
    print(fib2(3))
    print(fib2(4))
    print(fib2(5))
    print(fib2(6))
