'''
Given an array nums of distinct positive integers, 
return the number of tuples (a, b, c, d) such that a * b = c * d 
where a, b, c, and d are elements of nums, and a != b != c != d.
'''

def tupleSameProduct(nums):

    product_map = {}  
    count = 0
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            product = nums[i] * nums[j]
            if product in product_map:
                count += product_map[product] * 8  

            if product in product_map:
                product_map[product] += 1
            else:
                product_map[product] = 1

    return count        

print(tupleSameProduct([1,2,4,5,10]))

#8