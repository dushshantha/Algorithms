def switchBits(x, i, j):
    print(bin(x))
    print(bin(x ^ ((1 << i) | (1 << j))))
    x = x ^ ((1 << i) | (1 << j))
    return x

def reverse(x, l):
    i = 0
    j = l - 1
    while i < j:
        #print(i,j)
        x = switchBits(x, i,j)
        i += 1
        j -= 1
    return x
    #print(bin(x))

def reverse64Bit(x):
    cache = []
    maskLen = 16
    mask = 0xFFFF
    print(bin(x))
    cache.append(reverse(x & (mask), maskLen))
    for i in range(1,4):
        cache.append(reverse((x & (mask << (maskLen * i))), maskLen))

    print(cache)

    ret = cache[0] << (maskLen * 3) | cache[1] << (maskLen * 2) | cache[2] << (maskLen) | cache[0]
    print(bin(ret))
    return ret


if __name__ == '__main__':
    print('Switching bits')
    print(bin(switchBits(1123, 1,2)))
    #print(bin(12 & (1 << 2)))

    x = 1242342
    #print(reverse64Bit(x))
