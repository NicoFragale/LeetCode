'''
You are given a string word. A letter is called special if it appears both in lowercase and uppercase in word.

Return the number of special letters in word.
'''
def numberOfSpecialChars(word):
    wordset = set(word)
    word = ''.join(wordset)
    print(word)
    contatore = 0 
    for letter in word: 
        if letter == letter.lower():
            if letter.upper() in word: 
                contatore += 1
    return contatore 
print(numberOfSpecialChars('aaAbcBC'))