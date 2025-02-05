'''
Given an integer array nums and an integer k, return the number of pairs (i, j) where i < j such that |nums[i] - nums[j]| == k.

The value of |x| is defined as:

x if x >= 0.
-x if x < 0.
'''

def countKDifference(nums, k):
    c = 0 
    for i, num1 in enumerate(nums): 
        for num2 in nums[i+1:]:
            if abs(num1-num2) == k: 
                c+=1
    return c


print(countKDifference([1,2,2,1], 1))