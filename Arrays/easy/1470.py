'''
Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].

Return the array in the form [x1,y1,x2,y2,...,xn,yn].
'''

def shuffle(nums, n):
    n1 = nums[:n]
    n2 = nums[n:]
    o = []
    for i in range(len(n1)):
        o.append(n1[i])
        o.append(n2[i])
    return o 

print(shuffle([1,2,3,4,4,3,2,1], 4))