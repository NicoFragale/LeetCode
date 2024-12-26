#non completo 
def getSmallestString(s):
    stringa = ''
    for index, num in enumerate(s): 
        if int(num) %2 == 0 and index == 0: 
            if int(s[index+1]) %2 == 0 and num > s[index+1]: 
                stringa += s[index+1]
                stringa += num 
        if int(num) %2 == 0 and index == len(s)-1:
            
    return stringa
print(getSmallestString('45320'))