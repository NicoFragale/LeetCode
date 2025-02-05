'''
Given a string s, return true if s is a good string, or false otherwise.

A string s is good if all the characters that appear in s have the same number of occurrences (i.e., the same frequency).
'''

def areOccurrencesEqual( s):
    n = s.count(s[0])
    for let in s:
        if s.count(let) != n:
            return False
    return True
print(areOccurrencesEqual('ababc'))