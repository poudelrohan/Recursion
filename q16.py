'''
Given two arrays of numbers, merge them into one array using recursion.
They may be of un-equal lengths.
LOOKED UP ANSWER
'''

def merge_arr(a,b):
    if not a:
        return  b
    if not b:
        return a
    
    return [a[0]] + merge_arr(a[1:],b)

a = [1,2,3]
b = [4,5,6]

print(merge_arr(a,b))
    