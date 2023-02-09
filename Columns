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
