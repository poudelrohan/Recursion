'''
Extend 17 so that the output returns a string containing no duplicates. 
Example f(”aabbcc”) → “abc” and  f(”abbcb”) → “abc”. 
The order of characters doesn’t matter.

LOOKED UP
'''

def remove_all_duplicates(s,seen=set()):
    if not s:
        return ""
    
    if s[0] not in seen:
        seen.add(s[0])
        return s[0] + remove_all_duplicates(s[1:], seen)
    else:
        return remove_all_duplicates(s[1:], seen)
    
strr = 'aabdcdce'
print(remove_all_duplicates(strr))

        