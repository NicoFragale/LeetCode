'''
You are given a string s. The score of a string is defined as the sum of the absolute difference between the ASCII values of adjacent characters.

Return the score of s.
'''
def scoreOfString(s):
    c = 0
    for index, numero in enumerate(s[:-1]):
        succ = index+1
        c += abs(ord(s[index])- ord(s[succ]))
    return c
print(scoreOfString('hello'))