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
