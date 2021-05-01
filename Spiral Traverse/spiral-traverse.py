def spiralTraverse(array):
    # Write your code here.
    start_row = 0
    end_row = len(array) - 1
    start_col = 0
    end_col = len(array[start_row]) - 1

    result = []
    while start_row <= end_row and start_col <= end_col:

        for col in range(start_col, end_col+1):
            result.append(array[start_row][col])

        for row in range(start_row+1, end_row+1):
            result.append(array[row][end_col])

        for col in reversed(range(start_col, end_col)):
            if(start_row == end_row):
                break
            result.append(array[end_row][col])

        for row in reversed(range(start_row+1, end_row)):
            if(start_col == end_col):
                break
            result.append(array[row][start_col])

        start_row += 1
        end_row -= 1
        start_col += 1
        end_col -= 1

    return result
