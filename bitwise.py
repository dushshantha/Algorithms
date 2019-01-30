import math
import random

def countBits(x):
    bit_count = 0

    while x:
        bit_count +=  x & 1
        x >>= 1
    print(bit_count)

def switchBits(x, i, j):
    print(bin(x))
    bit_mask = (1 << i) | (1 << j)
    print(bin(x ^ bit_mask))

def reverse64(x):
    mask = 0xFFFF
    mask_len = 16

    first16 = x & mask
    second16 = (x >> mask_len) & mask
    third16 = (x >> (mask_len * 2)) & mask
    forth16 = (x >> (mask_len * 3)) & mask

    return (first16 ^ mask ) << (3 * mask_len) | (second16 ^ mask ) << (2 * mask_len) | (third16 ^ mask ) << mask_len | (forth16 ^ mask)



if __name__ == "__main__":
    countBits(12)
    print(math.ceil(3.4))
    print(float('inf'))
    print(random.randint(8,16))
    switchBits(6, 0,2)
    print(bin(0xFFFF))
    print(bin(6723469834))
    print(bin(reverse64(6723469834)))
