'''
You are given a binary string s and an integer k.

A binary string satisfies the k-constraint if either of the following conditions holds:

The number of 0's in the string is at most k.
The number of 1's in the string is at most k.
Return an integer denoting the number of 
substrings
 of s that satisfy the k-constraint.
'''
def countKConstraintSubstrings(s,k):
    c = 0 
    lista = []
    n = len(s)
    for i in range(n):  
        for j in range(i + 1, n + 1):  
            lista.append(s[i:j])

    for stringa in lista: 
        zeri = stringa.count('0')
        uni =  stringa.count('1')
        if zeri <= k or uni <= k:
            c += 1

    return c
    
    

print(countKConstraintSubstrings('10101', 1))