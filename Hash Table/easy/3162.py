'''
You are given 2 integer arrays nums1 and nums2 of lengths n and m respectively. You are also given a positive integer k.
A pair (i, j) is called good if nums1[i] is divisible by nums2[j] * k (0 <= i <= n - 1, 0 <= j <= m - 1).
Return the total number of good pairs.
'''

def numberOfPairs(nums1, nums2, k):
    c = 0
    n, m = len(nums1), len(nums2)
    for i in range(n):
        for j in range(m):
            divisor = nums2[j] * k
            if nums1[i] % divisor == 0:
                print((i,j))
                c += 1
    return c
print(numberOfPairs([1,2,4,12], [2,4], 3))

#oppure return sum(1 for x in nums1 for y in nums2 if x % (y * k) == 0)
