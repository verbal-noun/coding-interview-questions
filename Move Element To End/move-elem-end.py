def moveElementToEnd(array, toMove):
    # Write your code here.
    start = 0
    end = len(array) - 1
    while start < end:
        if array[start] == toMove:
            array[start], array[end] = array[end], array[start]
            end -= 1
        else:
            start += 1

    return array
