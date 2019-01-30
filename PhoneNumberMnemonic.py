map = ['0', '1', 'ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

def mnemonic_maker(n):
    
    partial_mnemonic = [0] * len(n)
    mnemonics = []

    def form_mnemonic(digit):
        if digit == len(n):
            mnemonics.append(''.join(partial_mnemonic))

        else:
            for c in map[int(n[digit])]:
                partial_mnemonic[digit] = c
                form_mnemonic(digit + 1)
    
    form_mnemonic(0)
    return mnemonics

if __name__ == "__main__":
    print(mnemonic_maker('223'))
    
    
