'''
Given a m x n matrix grid which is sorted in non-increasing order both row-wise and column-wise, 
return the number of negative numbers in grid.
'''

def countNegatives(grid):
    c = 0
    maxI = len(grid[0]) 
    for index,lista in enumerate(grid):
        for i in range(maxI):
            if lista[i]<0:
                c += len(grid)- index
                maxI -=1
            else:
                continue 
    return c



print(countNegatives([[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]))