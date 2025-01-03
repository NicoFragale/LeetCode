'''
You're given strings jewels representing the types of stones that are jewels, and stones representing the stones you have. Each character in stones is a type of stone you have. You want to know how many of the stones you have are also jewels.

Letters are case sensitive, so "a" is considered a different type of stone from "A".
'''

def numJewelsInStones( jewels, stones):
    c = 0
    for l in stones: 
        if l in jewels:
            c +=1
    return c

print(numJewelsInStones("aA","aAAbbbb"))