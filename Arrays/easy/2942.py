'''
You are given a 0-indexed array of strings words and a character x.

Return an array of indices representing the words that contain the character x.

Note that the returned array may be in any order.
'''

def findWordsContaining(words, x):
    lista = []
    for index, stringa in enumerate(words): 
        if x in stringa: 
            lista.append(index)
    return lista
print(findWordsContaining(["abc","bcd","aaaa","cbc"],"a"))