def rotate(matrix): 
    size = len(matrix) -1 

    # Rotate layer by layer 
    for layer in range(0, len(matrix) // 2):
        for i in range(layer, size - layer):

            # Declare the corners 
            top = matrix[layer][i]
            right = matrix[i][size - layer]
            bottom = matrix[size - layer][size - i]
            left = matrix[size - i][layer]

            # Walk through corners 
            matrix[i][size - layer] = top
            matrix[size - layer][size - i] = right
            matrix[size - i][layer] = bottom 
            matrix[layer][i] = left

    
    return matrix