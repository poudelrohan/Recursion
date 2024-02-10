'''
Given a large number N in string form (”123445”) compute the sum of each digit in the number.
'''
def sum_string(s):
    if len(s) == 1:
        return int(s)
    return int(s[0]) + sum_string(s[1:])

num = "12345"
print(sum_string(num))