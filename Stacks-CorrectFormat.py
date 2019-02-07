
def correctFormat(s):
    st = []
    memo = {'(': ')', '[' : ']', '{' : '}'}

    for c in s:
        if c in memo:
            st.append(c)
        elif len(st) == 0 or memo[st.pop()] != c:
            return False
    #print(st)
    return not st

if __name__ == "__main__":
    assert correctFormat("()([]{})") == True ,"Fail"
    assert correctFormat("()([{})") == False ,"Fail"