'''
Write a recursive function that takes a string S and returns
a string with all consecutive duplicates removed. 
Example f(”aabbcc”) → “abc” and  f(”abbcb”) → “abcb”
'''

def remove_duplicates(s):
    if len(s) <= 1:
        return s
    
    if s[0] == s[1]:
        return remove_duplicates(s[1:])
    return s[0] + remove_duplicates(s[1:])

a = "aabbcdd"

print(remove_duplicates(a))