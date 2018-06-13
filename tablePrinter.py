tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]


colWidths = [0] * len(tableData)
for i in range(len(tableData)): #i = 0, 1, 2
    for ii in range(len(tableData[i])): #ii = 0, 1, 2, 3
        if colWidths[i] < len(tableData[i][ii]):
            colWidths[i] = len(tableData[i][ii])


outerListLength = 0
innerListLength = 0
while innerListLength < len(tableData[outerListLength]):
    i = 0
    print(tableData[i][innerListLength].rjust(colWidths[i]), tableData[i+1][innerListLength].rjust(colWidths[i+1]), tableData[i+2][innerListLength].rjust(colWidths[i+2]))
    innerListLength += 1
