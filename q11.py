'''
given a string S, and a character C, count the occurrence of character C in the string using recursion. 
Return a number.
'''
def char_count(s,c):
    if len(s) == 0:
        return 0
    elif s[0] == c:
        return 1 + char_count(s[1:],c)
    else:
        return char_count(s[1:],c)
    
    
print(char_count("helloworld",'l'))