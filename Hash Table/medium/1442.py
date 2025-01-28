'''
Given an array of integers arr.

We want to select three indices i, j and k where (0 <= i < j <= k < arr.length).

Let's define a and b as follows:

a = arr[i] ^ arr[i + 1] ^ ... ^ arr[j - 1]
b = arr[j] ^ arr[j + 1] ^ ... ^ arr[k]
Note that ^ denotes the bitwise-xor operation.

Return the number of triplets (i, j and k) Where a == b.
'''

def countTriplets(arr):
    
    triplets_count = 0
    xor_map = {} 
    xor_cumulative = 0
    
    for k in range(len(arr)):
        xor_cumulative ^= arr[k] #XOR until now

        if xor_cumulative == 0: #if 0 
            triplets_count += k #there are k triplets

        if xor_cumulative in xor_map: #then there is a second side equal and x ^ x is 0 
            triplets_count += xor_map[xor_cumulative][1]  
            xor_map[xor_cumulative] = (xor_map[xor_cumulative][0] + 1,  xor_map[xor_cumulative][1] + k  )
    
        else:
            xor_map[xor_cumulative] = (1, k) #1 time it appears, k is the index 

    return triplets_count

print(countTriplets([2, 3, 1, 6, 7])) 
