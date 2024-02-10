'''
Given an array, return the max number in the array using recursion.
'''

def max_num(ar):
    if not ar:
        return float('-inf')
    return max(ar[0],max_num(ar[1:]))
    
    
    
    
list_a = [1,2,3,4,5,12]

print(max_num(list_a))