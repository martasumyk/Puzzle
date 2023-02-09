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
