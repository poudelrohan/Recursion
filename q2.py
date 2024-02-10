'''
Compute the sum of first N natural numbers. sum_natural_recursive(N) → 0 + 1  + 2 + … + N
'''
n = 5
def sum_natural_recursive(num):
    if( num == 1):
        return 1
    return num + sum_natural_recursive(num-1)
    
print(sum_natural_recursive(n))
