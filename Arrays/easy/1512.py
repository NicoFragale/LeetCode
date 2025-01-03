'''
Given an array of integers nums, return the number of good pairs.

A pair (i, j) is called good if nums[i] == nums[j] and i < j.
'''
def numIdenticalPairs(nums):
    lista = []
    for i1, n1 in enumerate(nums): 
        for i2, n2 in enumerate(nums[i1+1:]):
            if n2==n1: 
                t = (i1,i2)
                lista.append(t)
    return len(lista)
print(numIdenticalPairs([1,2,3,1,1,3]))
