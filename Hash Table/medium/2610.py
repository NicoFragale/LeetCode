'''
You are given an integer array nums. You need to create a 2D array from nums satisfying the following conditions:

The 2D array should contain only the elements of the array nums.
Each row in the 2D array contains distinct integers.
The number of rows in the 2D array should be minimal.
Return the resulting array. If there are multiple answers, return any of them.

Note that the 2D array can have a different number of elements on each row.
'''
def findMatrix(nums):
    hashtable = dict()
    for num in nums:  
        if num not in hashtable: 
            hashtable[num] = 1
        else: 
            hashtable[num] += 1

    output = []
    for x in range(max(hashtable.values())):
        output.append([])

    for chiave, valore in hashtable.items():
        for i in range(valore):
            output[i].append(chiave)
    
    return output
    
print(findMatrix([1,3,4,1,2,3,1]))