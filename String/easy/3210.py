'''
You are given a string s and an integer k. Encrypt the string using the following algorithm:

For each character c in s, replace c with the kth character after c in the string (in a cyclic manner).
Return the encrypted string.
'''
def getEncryptedString(s,k):
    new_stringa = ''
    new_index = 0 
    for index,lettera in enumerate(s): 
        new_index = (index + k) % len(s)
        new_stringa += s[new_index]
    return new_stringa
print(getEncryptedString('dart', 3))