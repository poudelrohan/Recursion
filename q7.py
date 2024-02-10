'''
Calculate the sum of odd numbers in an array using recursion. 
sum_odd_recursive(arr) → return sum of odd numbers in the array

'''
def sum_odd_recursion(arrr):
    if len(arrr) == 0:
        return 0
    elif arrr[0] % 2 == 0:
        return 0 + sum_odd_recursion((arrr[1:]))
    elif arrr[0] % 2 != 0:
        return arrr[0] + sum_odd_recursion((arrr[1:]))
        


list_a = [0,1,2,3,4,5,6]
print(sum_odd_recursion(list_a))

