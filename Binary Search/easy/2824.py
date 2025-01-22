'''
Given a 0-indexed integer array nums of length n and an integer target, return the number of pairs (i, j)
 where 0 <= i < j < n and nums[i] + nums[j] < target.
'''

def countPairs(nums, target):

    nums = sorted(nums)
    sx,c,dx = 0,0, len(nums)-1
    while sx < dx:
        if (nums[sx] + nums[dx]) < target:
            c += (dx-sx)
            sx += 1
            dx = len(nums)-1
        else:
            dx -=1
    return c 

print(countPairs([-6,2,5,-2,-7,-1,3],-2))