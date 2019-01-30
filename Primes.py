import math
def is_prime(n): 
    #print(int(math.sqrt(n))) 
    for i in range(2, int(math.sqrt(n))+ 1):
        if n % i == 0:
            return False
    return True

def list_primes(n):
    r = []

    for i in range(2, n + 1):
        if is_prime(i):
            r.append(i)
    return r
    
if __name__ == "__main__":
    print(is_prime(1))
    print(is_prime(2))
    print(is_prime(3))
    print(is_prime(4))
    print(is_prime(6))
    print(is_prime(5))

    print(list_primes(18))
    print(list_primes(6))