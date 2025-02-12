'''
Given three integer arrays nums1, nums2, and nums3, return a distinct array containing all the values that are present in at least two out of the three arrays. You may return the values in any order.
'''

def twoOutOfThree(nums1, nums2, nums3):

    output = list()
    for n1 in nums1:
        for n2 in nums2: 
            if n1==n2: 
                output.append(n1)
    
    output2 = list()
    for n1 in nums1:
        for n2 in nums3: 
            if n1==n2: 
                output2.append(n1)

    output3 = list()
    for n1 in nums2:
        for n2 in nums3: 
            if n1==n2: 
                output3.append(n1)
    
    return max(output,output2, output3)

print(twoOutOfThree([1,1,3,2], [2,3], [3]))

'''
Meglio cosi: 
def twoOutOfThree(self, nums1, nums2, nums3):
        intersection= list(set(nums1)&set(nums2))
        intersection2= list(set(nums2)&set(nums3))
        intersection3= list(set(nums1)&set(nums3))
        intersection1 = list(set(intersection + intersection2 + intersection3))
        return(intersection1)

spiegami questa soluzione
'''