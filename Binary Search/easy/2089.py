'''
You are given a 0-indexed integer array nums and a target element target.

A target index is an index i such that nums[i] == target.

Return a list of the target indices of nums after sorting nums in non-decreasing order. If there are no target indices, return an empty list. The returned list must be sorted in increasing order.

NON CAPISCO IL SENSO DELLA RICERCA BINARIA
'''
def targetIndices(nums, target):
    nums = sorted(nums)
    lista = []
    for index, numero in enumerate(nums):
        if numero == target:
            lista.append(index)
    return lista 
print(targetIndices([1,2,5,2,3], 2))