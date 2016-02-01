data1 = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]


def printTable(tableData):
    
#set the default column width to [0,0,0]
    colWidths = [0] * len(tableData)

#check the length of each string in nested lists
#then compare with the default column width
#if the compared value is greater than the default value
#default value will be re-assigned
    
    for column in range(len(tableData)):
        for items in range(len(tableData[column])):
            if len(tableData[column][items]) > colWidths[column]:
                colWidths[column] = len(tableData[column][items])

#print the table with right justified by 2 to make it look nicer
                
    for i in range(len(tableData[0])):
        for k in range(len(tableData)):
            print(tableData[k][i].rjust(colWidths[k]+2), end = ' ')
        print()
        
printTable(data1)          










    
 




