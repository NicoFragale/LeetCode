'''
You are given a string allowed consisting of distinct characters and an array of strings words. A string is consistent if all characters in the string appear in the string allowed.

Return the number of consistent strings in the array words.
'''

def countConsistentStrings( allowed, words):
    c = len(words)
    for word in words: 
        for l in word: 
            if l not in allowed:
                c-=1
                break 
    return c


print(countConsistentStrings("fstqyienx",["n","eeitfns","eqqqsfs","i","feniqis","lhoa","yqyitei","sqtn","kug","z","neqqis"]))