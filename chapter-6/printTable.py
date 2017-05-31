'''
Table Printer
Write a function named printTable() that takes a list of lists of strings
and displays it in a well-organized table with each column right-justified.
Assume that all the inner lists will contain the same number of strings.
For example, the value could look like this:
tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

Your printTable() function would print the following:
          apples Alice dogs
         oranges   Bob cats
        cherries Carol moose
          banana David goose

Hint: Your code will first have to find the longest string in each of the
inner lists so that the whole column can be wide enough to fit all the strings.
You can store the maximum width of each column as a list of integers. The
printTable() function can begin with colWidths = [0] * len(tableData), which
will create a list containing the same number of 0 values as the number
of inner lists in tableData. That way, colWidths[0] can store the width of the
longest string in tableData[0], colWidths[1] can store the width of the longest
string in tableData[1], and so on. You can then find the largest value in
the colWidths list to find out what integer width to pass to the rjust() string
method.

'''

tableData = [['apples', 'oranges', 'cherries', 'bananas'],
             ['Alice', 'Bob', 'Carol', 'David',],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable(table):
    colWidths = [0] * len(table) #This statement initializes our colWidth list i.e. [0, 0, 0]. Without initialization, we will receive 'out of index' error while trying to assign it a value

    for i in range(len(table)): # i.e. 0, 1, 2
        for k in range(len(table[0])): # i.e. 0, 1, 2, 3
            colWidths[i] = len(max(table[i], key=len)) #The builtin 'max' function returns the longest string in the list. We then take the length of the string to get the colWidth value

    for x in range(len(table[0])): # i.e. 0, 1, 2, 3
        for y in range(len(table)): # i.e. 0, 1, 2
            # Print the value and apply right justification (+ 1 in colWidth is to give a space separation between the columns. 'end' parameter will skip the new line in print.
            print(table[y][x].rjust(colWidths[y] + 1), end = '')
        print() # After the inner loop, we are printing a new line for the outer loop

printTable(tableData)
