'''
You are given a string num consisting of only digits. A string of digits is called balanced if the sum of the digits at even indices is equal to the sum of digits at odd indices.
Return true if num is balanced, otherwise return false.
'''

def isBalanced(num):
    odd, even = 0, 0
    for i, n in enumerate(num): 
        if i%2==0: 
            even += int(n)
        else: 
            odd += int(n)
    if odd == even: 
        return True 
    
    return False
print(isBalanced('1234'))