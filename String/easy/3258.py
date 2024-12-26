#non concluso 
def countKConstraintSubstrings(s,k):
    output = ''
    i = 0 
    l = []
    for index, bin in enumerate(s): 
        output += bin
        i += 1
        l.append(output)
        for b2 in s[index+1:]:
            output += b2

            for numero in output: 
                r = output.count(numero)
                if output.count(numero) <= k:
                    i += 1
                    l.append(output)

    return i, l

print(countKConstraintSubstrings('10101', 1))