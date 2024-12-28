'''
A word is considered valid if:

It contains a minimum of 3 characters.
It contains only digits (0-9), and English letters (uppercase and lowercase).
It includes at least one vowel.
It includes at least one consonant.
'''
def isValid(word):
        word.lower()
        num = '0123456789'
        letters = 'qwertyuiopasdfghjklzxcvbnm'
        vocali = 'aeiou'
        conditions = [False, False, False, False]
        if len(word) >=3:
            conditions[0] = True
        for letter in word: 
            letter = letter.lower()
            if letter in vocali: 
                conditions[1] = True 
            elif letter in letters:
                conditions[2] = True
            elif letter in num: 
                conditions[3] = True 
            elif letter not in letters and letter not in num:
                return False
        if all(conditions): return True
        else: return False
print(isValid('aya'))