'''
Given a large integer N, compute the sum of each digit in the number (eg: 12345 → 1 + 2 + … + 5)
'''
def sum_digit(num):
    if num == 0:
        return 0
    return (num % 10) + sum_digit(num // 10)

n = 3

print(sum_digit(n))
