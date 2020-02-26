#Using Eucledian algorithm 
def GCD(a, b):
    if b == 0:
        return a
    else:
        a_p = a % b
        return GCD(b, a_p)

print(GCD(3918848,1653264))
print(GCD(357,234))