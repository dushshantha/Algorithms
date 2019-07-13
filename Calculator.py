# You are building an educational website and want to create a simple calculator for students to use. The calculator will only allow addition and subtraction of non-negative integers.

# We also want to allow parentheses in our input. Given an expression string using the "+", "-", "(", and ")" operators like "5+(16-2)", write a function to parse the string and evaluate the result.

# Sample output:
#   calculate("5+16-((9-6)-(4-2))+1") => 21
#   calculate("22+(2-4)") => 20
#   calculate("6+9-12") => 3
#   calculate("((1024))") => 1024

def calculate_simple(e):
    i = 0
    first = ''
    ret = 0
    while i < len(e) and ord(e[i]) >= ord('0') and ord(e[i]) <= ord('9'):
        first += e[i]
        i += 1
    
    ret = int(first)
    
    while i < len(e):
        exp = e[i]
        i += 1
        second = ''
        while i < len(e) and ord(e[i]) >= ord('0') and ord(e[i]) <= ord('9'):    
            second += e[i]
            i += 1
        
        if exp == '+':
            ret = ret + int(second)
        if exp == '-':
            ret = ret - int(second)
            
    
    return ret


def calculate(e):
    stack = []
    parent = []
    
    i = 0
    
    while i < len(e):
        if e[i] == '(':
            stack.append(e[i])
            i += 1
            
            while i < len(e) and e[i] != ')':
                while i < len(e) and ord(e[i]) >= ord('0') and ord(e[i]) <= ord('9'):
                    num += e[i] 
                    i += 1
                stack.append(num)
                i += 1
        
            elif e[i] == ')':
            
        
        else:
            num = ''
            exp = '+'
            while i < len(e) and ord(e[i]) >= ord('0') and ord(e[i]) <= ord('9'):
                num += e[i] 
                i += 1
            
            if exp == '+':
                parent.insert(0,0 + int(num))
            if exp == '-':
                parent.insert(0,0 - int(num))
            
            exp = e[i]
    
def calculate