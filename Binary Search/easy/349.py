'''
Given two integer arrays nums1 and nums2, return an array of their
intersection
. Each element in the result must be unique and you may return the result in any order.
'''

def intersection(nums1, nums2):

    nums1 = sorted(nums1)
    nums2 = sorted(nums2)
    sx1, sx2 = 0,0
    dx1, dx2 = len(nums1) -1, len(nums2)-1
    output = set()
    #m = min(nums1, nums2)
    
    while True: 
        if sx1 > dx1 or sx2> dx2: break
        if nums1[sx1] == nums2[sx2]:
            output.add(nums1[sx1])
            sx1 += 1
            sx2 += 1
        elif nums1[sx1] > nums2[sx2]:
            sx2 += 1
        elif nums1[sx1] < nums2[sx2]:
            sx1 += 1


        
    return list(output)
print(intersection([1,2,2,1], [2,2]))   