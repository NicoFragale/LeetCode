def clearDigits(s):
    new_stringa = ''
    index = 0 
    for numero in s: 
        if numero.isdigit() == True: 
            if index == 0: 
                index += 1
                continue 

            elif s[index-1].isdigit() == False: 
                s = s[:index-1] +s[index+1:]
                index -=1
            else: 
                index += 1
        else:
            index +=1
    return s

print(clearDigits('gbysb5'))