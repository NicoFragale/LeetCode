'''

'''

def getSneakyNumbers(nums):
    l = set()
    for n in nums: 
        x = nums.count(n)
        if x > 1:
            l.add(n)
    return list(sorted(l))


print(getSneakyNumbers([0,3,2,1,3,2]))