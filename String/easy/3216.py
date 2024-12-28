'''
Given a string s containing only digits, return the
lexicographically smallest string
 that can be obtained after swapping adjacent digits in s with the same parity at most once.

Digits have the same parity if both are odd or both are even. For example, 5 and 9, as well as 2 and 4, have the same parity, while 6 and 9 do not.
'''
def getSmallestString(s):
    stringa = ''

    for index, numero in enumerate(s[:-1]):
        succ = index+1

        if numero == '0' or s[succ] == '0':
            continue

        elif int(s[index])%2 == 0 and int(s[succ])%2 == 0:
            if s[index] > s[succ]: 
                lista = list(s)
                lista[index], lista[succ] = lista[succ], lista[index]
                s = ''.join(lista)
                break

        elif int(s[index])%2 == 1 and int(s[succ])%2 == 1:
            if s[index] > s[succ]: 
                lista = list(s)
                lista[index], lista[succ] = lista[succ], lista[index]
                s = ''.join(lista)
                break
        else: continue 
    return s
print(getSmallestString('45320'))