'''
count_down_recursive(N) → prints N, N-1, N-2 …. 3. 2, 1, 0 in new line
'''

n = 5

def count_down_recursive(num):
    if num >= 0:
        print(num)
        return(count_down_recursive(num-1))
    
count_down_recursive(n)
