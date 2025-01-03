'''
A decimal number is called deci-binary if each of its digits is either 0 or 1 without any leading zeros. For example, 101 and 1100 are deci-binary, while 112 and 3001 are not.

Given a string n that represents a positive decimal integer, return the minimum number of positive deci-binary numbers needed so that they sum up to n.
'''

def minPartitions(n):
    s = str(n)
    MaxS = max(list(s))
    c = 0 

    for i in range(int(MaxS)): 
        subb  = ''
        for numero in s: 
            if int(numero) > 0: 
                subb += '1'
            else: 
                subb += '0'
        x = int(s)
        x -= int(subb)
        s = str(x)
        c += 1
    return c
print(minPartitions(32))