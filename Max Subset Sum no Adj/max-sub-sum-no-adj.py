def maxSubsetSumNoAdjacent(array):
    # Write your code here.
    if(len(array) < 1):
        return 0

    if(len(array) < 3):
        return max(array)

    running_sum = [0 for i in range(len(array))]

    running_sum[0], running_sum[1] = array[0], array[1]

    for curr_idx in range(2, len(array)):
        max_sum = 0
        for i in range(0, curr_idx-1):
            max_sum = max(running_sum[i], max_sum)

        running_sum[curr_idx] = max_sum + array[curr_idx]

    return max(running_sum)


"""
    [75 105 120 75 90 135]
	
	[75 105 195 195 0 0]
	
	75 
	
	
	Notes: 
	[75  105  195   180  210  330]
	
	for each index before curr - 1, take the max and add it to current
	
	
			 		      
"""
