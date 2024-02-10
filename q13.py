'''
Given a string/array, compute its length using recursion. You are not allowed to use len() function.
'''
def compute_len(s):
    if not s:
        return 0
    return 1 + compute_len(s[1:])

lista = "string"
listb = [1,2,3,4,5,6,0]

print(compute_len(lista))
print(compute_len(listb))