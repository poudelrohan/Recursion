'''
Check if a string is palindrome or not using recursion. 
is_palindrome_recursive(S) → returns whether S is palindrome or not

'''
def is_palindrome_recursive(S):
    if len(S) == 0 or len(S) == 1:
        return True
    
        
    if S[0] == S[-1]:
        return is_palindrome_recursive(S[1:-1])
    return False

a = 'heleh'
print(is_palindrome_recursive(a))
        
    
    
    