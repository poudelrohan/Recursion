'''
Calculate the sum of an array using recursion. sum_recursive(arr) → returns sum of array

'''
def sum_recursion(arrr):
    if len(arrr) == 0:
        return 0
    return arrr[0] + sum_recursion(arrr[1:])


list_a = [0,1,2,3,4,5,6]
print(sum_recursion(list_a))
