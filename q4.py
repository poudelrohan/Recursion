'''
compute power of x to N (x^N) using recursion. power_x_to_n_recursive(x, n) returns x^n

'''
def power_x_to_n_recursive(a,b):
    if b == 0:
        return 1
    elif b == 1:
        return a
    return a* power_x_to_n_recursive(a,b-1)
    
print(power_x_to_n_recursive(3,0))