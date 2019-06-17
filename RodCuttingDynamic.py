import time
def cutRod_recursive(p, n): 
    if n == 0:
        return 0    
    r = 0
    for i in range(1, n + 1, 1):
        r =max(r, p[i] + cutRod_recursive(p, n- i))
    
    return r

def cutRod_memorized(p,n):
    m = [-1]* (n + 1)
    m[0] = 0
    return cutRod_dynamic(p,n, m)

def cutRod_dynamic(p, n, m):
    if m[n] >= 0:
        return m[n]
    r = -1
    for i in range(1,n+1, 1):
        r = max(r, p[i] + cutRod_dynamic(p, n - i, m))
    m[n] =  r
    return r

def cutRod_BottomUp(p, n):
    m = [-1] * (n+ 1)
    # Solution
    s = [0] * (n + 1)
    m[0] = 0
    for j in range(1, n + 1, 1):
        r = -1
        for i in range(1, j + 1, 1):
            if r < p[i] + m[j-i]:
                r = p[i] + m[j-i]
                s[j] = i
        m[j] = r
    print(s)
    sol = []
    l = n
    while l > 0:
        sol.append(s[l])
        l -= s[l]

    return m[n], sol

if __name__ == "__main__":
    p = [0,1,5,8,9,10,17,17,20,24,30]
    start = time.time()
    print(cutRod_recursive(p, 5))
    end = time.time()
    print('Time elapsed cutRod_recursive: ', end - start)

    start = time.time()
    print(cutRod_memorized(p, 5))
    end = time.time()
    print('Time elapsed cutRod_mem_dynamic: ', end - start)

    start = time.time()
    print(cutRod_BottomUp(p, 5))
    end = time.time()
    print('Time elapsed cutRod_BottomUp: ', end - start)