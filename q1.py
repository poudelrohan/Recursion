'''
Q1)
Compute factorial of a number using recursion. N! = N * (N-1) * (N-2) * …. * 1, 0! = 1! = 1. 
factorial_recursive(N) → returns N!
'''


n = 3
def factorial_recursive(num):
    if(num == 0 or num == 1):
        return 1
    return num * factorial_recursive(num-1)

print(factorial_recursive(n))