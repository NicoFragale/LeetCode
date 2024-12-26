'''You are given a string s. Simulate events at each second i:

If s[i] == 'E', a person enters the waiting room and takes one of the chairs in it.
If s[i] == 'L', a person leaves the waiting room, freeing up a chair.
Return the minimum number of chairs needed so that a chair is available for every person who enters the waiting room given that it is initially empty.'''
def minimumChairs(s):
    lista = []
    m = []
    stringa = ''
    i = 0 
    while i < len(s): 
        if i == 0:
            stringa += s[i]
        elif s[i] in stringa: 
            stringa += s[i]
        elif s[i] not in stringa: 
            lista.append(stringa)
            stringa = s[i]
        i += 1
    lista.append(stringa)
    contatore = 0
    for index, stringa in enumerate(lista): 
        if stringa[0] == 'E':
            contatore += len(stringa)
            m.append(contatore)
        elif stringa[0]== 'L' and index == 0:
            continue
        elif stringa[0]== 'L' and index !=len(lista)-1: 
            contatore -= len(stringa)
            m.append(contatore)
    return max(m) 
print(minimumChairs('EEEEEELELLLE'))
