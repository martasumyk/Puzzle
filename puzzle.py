def rows(board: list) -> bool:
    '''
    Checks if rows in board are filled correctly.
    >>> rows(board = [\
    "**** ****",\
    "***1 ****",\
    "**  3****",\
    "* 4 1****",\
    "     9 5 ",\
    " 6  83  *",\
    "3   1  **",\
    "  8  2***",\
    "  2  ****"])
    True
    '''
    for k in board:
        for i in k:
            integers = []
            if i.isdigit():
                integers.append(i)
            if len(integers) != len(set(integers)):
                return False
    return True
    
def columns(board: list) -> bool:
    '''
    Checks if columns in board are filled correctly.
    >>> columns(board = [\
    "**** ****",\
    "***1 ****",\
    "**  3****",\
    "* 4 1****",\
    "     9 5 ",\
    " 6  83  *",\
    "3   1  **",\
    "  8  2***",\
    "  2  ****"])
    False
    '''
    for i in range(9):
        column = []
        for k in board:
            column.append(k[i])
        numbers = []
        for k in column:
            if k.isdigit():
                numbers.append(k)
        if len(numbers) != len(set(numbers)):
            return False
    return True

def colors(board: list) -> bool:
    '''
    Checks if the numbers of the same color is situated correctly.
    >>> colors(board = [\
    "**** ****",\
    "***1 ****",\
    "**  3****",\
    "* 4 1****",\
    "     9 5 ",\
    " 6  83  *",\
    "3   1  **",\
    "  8  2***",\
    "  2  ****"])
    False
    '''
    for i in range(5):
        color = []
        for k in range(5):
            color.append(board[k][4 - i])
            color.append(board[k][4 - i])
        numbers = []
        for j in color:
            if j.isdigit():
                numbers.append(j)
        if len(numbers) != len(set(numbers)):
            return False
    return True
 
def validate_board(board: list) -> bool:
    '''
    Checks if all the rules of filling the board are okey.
    >>> validate_board(board = [\
    "**** ****",\
    "***1 ****",\
    "**  3****",\
    "* 4 1****",\
    "     9 5 ",\
    " 6  83  *",\
    "3   1  **",\
    "  8  2***",\
    "  2  ****"])
    False
    '''
    return rows(board) and columns(board) and colors(board)



if __name__ == '__main__':
    import doctest
    print(doctest.testmod())