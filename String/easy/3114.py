'''
You are given a string s representing a 12-hour format time where some of the digits (possibly none) are replaced with a "?".

12-hour times are formatted as "HH:MM", where HH is between 00 and 11, and MM is between 00 and 59. The earliest 12-hour time is 00:00, and the latest is 11:59.

You have to replace all the "?" characters in s with digits such that the time we obtain by the resulting string is a valid 12-hour format time and is the latest possible.

Return the resulting string.
'''
def findLatestTime(s):
    new_s = ''

    if s[0] == '?' and s[1] == '?':
        new_s += '1' 
    elif s[0] == '?' and s[1] > '1':
        new_s += '0'
    elif s[0] == '?' and s[1] <= '1':
        new_s += '1'
    else: 
        new_s += s[0]

    if s[1] == '?' and new_s[0] == '1':
        new_s +=  '1' 
    elif s[1] == '?' and new_s[0] == '0':
        new_s += '9' 
    else: 
        new_s += s[1]

    new_s += ':'
    
    if s[3] == '?':
        new_s += '5' 
    else: 
        new_s += s[3]

    if s[4] == '?':
        new_s = new_s[:4] + '9' 
    else: 
        new_s += s[4]

    return new_s

print(findLatestTime('?1:?6'))