grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]
for ii in range(len(grid)): #for loop for bigger list (9)
    for i in range(len(grid[ii])): #for loop for inner list (6)
        if i < len(grid[ii]) - 1: #if i is less than 5
            print(grid[ii][i], end="") #then print all the values in a line
        else: #if i reached 5(last value in list)
            print(grid[ii][i]) #print value and add a line break
