'''
Given an integer array sorted in non-decreasing order, there is exactly one integer in the array that occurs more than 25% of the time, return that integer.
'''
def findSpecialInteger(arr):
    perc = 25/100 * len(arr) 
    for numero in arr: 
        x = arr.count(numero)
        if x > perc: 
            return numero

print(findSpecialInteger([1,2,2,6,6,6,6,7,10]))