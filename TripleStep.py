'''
A child is running up a staircase with n steps and can hop either 1, 2 or 3 steps at a time.
Implement a method to count how many possible ways the child can run up the stairs
'''

def countWays(n):
    memo = [0] * (n + 1)

    memo[0] = 1

    for i in range(1, len(memo)):
        for j in range(1, 4):
            if j <= i:
                memo[i] += memo[i - j]
    return memo[-1]


print(countWays(4))
print(countWays(3))