'''
You are given two 0-indexed integer permutations A and B of length n.

A prefix common array of A and B is an array C such that C[i] is equal to the count of numbers that are present at or before the index i in both A and B.

Return the prefix common array of A and B.

A sequence of n integers is called a permutation if it contains all integers from 1 to n exactly once.
'''

def findThePrefixCommonArray( A, B):
    output = []
    for index in range(len(A)):
        count = 0 
        lA = A[:index+1]
        lB = B[:index+1]
        for numero in lA: 
            if numero in lB:
                count += 1
        output.append(count)
    return output
        

print(findThePrefixCommonArray([1,3,2,4], [3,1,2,4]))

#Soluzione in O(n)
def prefix_common_array(A, B):
    seen_A = set()
    seen_B = set()
    result = []
    common_count = 0

    for i in range(len(A)):
        seen_A.add(A[i])
        seen_B.add(B[i])

        if A[i] in seen_B:
            common_count += 1
        if B[i] in seen_A and A[i] != B[i]:
            common_count += 1

        result.append(common_count)

    return result
