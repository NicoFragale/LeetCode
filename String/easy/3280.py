'''
You are given a string date representing a Gregorian calendar date in the yyyy-mm-dd format.

date can be written in its binary representation obtained by converting year, month, and day to their binary representations without any leading zeroes and writing them down in year-month-day format.

Return the binary representation of date.
'''
def convertDateToBinary(num):

    output = ''
    data = num.split('-')
    for index, numero in enumerate(data): 
        d = bin(int(numero))[2:]
        output+= d
        if index == len(data)-1: 
            return output
        else: 
            output += '-' 

print(convertDateToBinary('2080-02-29'))