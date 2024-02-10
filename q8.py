'''
Reverse a string using recursion reverse_recursive(S) → reversed string S’
'''
def reverse_recursive(S):
    if len(S) == 0 or len(S) == 1:
        return S
    elif len(S) > 1:
        return S[-1] + reverse_recursive(S[:-1])

strr = "1qsxwx"
print(reverse_recursive(strr))


        
    