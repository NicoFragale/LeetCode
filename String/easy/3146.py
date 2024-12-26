'''
You are given two strings s and t such that every character occurs at most once in s and t is a permutation of s.

The permutation difference between s and t is defined as the sum of the absolute difference between the index of the occurrence of each character in s and the index of the occurrence of the same character in t.

Return the permutation difference between s and t.
'''
def findPermutationDifference( s, t):
    l = []
    for index1, num1 in enumerate(s): 
        for index2, num2 in enumerate(t): 
            if num2 == num1: 
                diff = abs(index2-index1)
                l.append(diff)
    return sum(l)

print(findPermutationDifference('abcde', 'edbac'))