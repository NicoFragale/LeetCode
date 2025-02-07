'''
You are given 2 integer arrays nums1 and nums2 of lengths n and m respectively. You are also given a positive integer k.
A pair (i, j) is called good if nums1[i] is divisible by nums2[j] * k (0 <= i <= n - 1, 0 <= j <= m - 1).
Return the total number of good pairs.
'''

def numberOfPairs(nums1, nums2, k):
    c = 0 
    for i, n in enumerate(nums2): 
        nums2[i] *= k
    s = set(nums2)
    for n in nums1: 
        for n2 in s: 
            if n% n2==0: 
                c +=1
    return c
    
print(numberOfPairs([2,8,17,6], [3,1,1,8], 2))