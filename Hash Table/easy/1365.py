'''
Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it.
 That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].
Return the answer in an array.
'''


def smallerNumbersThanCurrent(self, nums):

        indexed_arr = list(enumerate(nums)) 
        indexed_arr.sort(key=lambda x: x[1])
        
        count_smaller = {}
        for i, (original_index, value) in enumerate(indexed_arr):
            if value not in count_smaller:
                count_smaller[value] = i
        
        result = [count_smaller[value] for index, value in enumerate(nums)]
        
        return result

