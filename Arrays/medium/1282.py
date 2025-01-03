'''
There are n people that are split into some unknown number of groups. Each person is labeled with a unique ID from 0 to n - 1.

You are given an integer array groupSizes, where groupSizes[i] is the size of the group that person i is in. For example, if groupSizes[1] = 3, then person 1 must be in a group of size 3.

Return a list of groups such that each person i is in a group of size groupSizes[i].

Each person should appear in exactly one group, and every person must be in a group. If there are multiple answers, return any of them. It is guaranteed that there will be at least one valid solution for the given input.
'''
def groupThePeople(groupSizes):
    output = []
    lista = []
    for numero in groupSizes: 
        l = [-1] * numero
        lista.append(l)
    
    for index, numero in enumerate(groupSizes): 
        for i1, l in enumerate(lista): 
            if len(l) == numero:
                for i2, n2 in enumerate(l): 
                    if n2 == -1:
                        l[i2] = index 
                        if i2 == len(l) -1:
                            output.append(l)
                            lista.pop(i1)
                        break
                break
    return  output
print(groupThePeople([3,3,3,3,3,1,3]))