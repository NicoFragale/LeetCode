'''
You are given two strings s1 and s2 of equal length. A string swap is an operation where you choose two indices in a string (not necessarily different) and swap the characters at these indices.

Return true if it is possible to make both strings equal by performing at most one string swap on exactly one of the strings. Otherwise, return false.
'''

def areAlmostEqual(s1, s2):

    lista = list(s2)
    i1 = 0 
    i2 = 1 
    while True: 
        l2 = lista[:]
        l2[i1] = lista[i2]
        l2[i2] = lista[i1]
        if l2 == list(s1):
            return True 
        if i2<len(lista)-1: 
            i2 +=1
        else: 
            i1 +=1
            i2 = i1 +1
            if i1 >= len(lista)-1:
                break
    return False
print(areAlmostEqual('attack', 'defend'))