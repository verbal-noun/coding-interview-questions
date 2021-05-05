def hasSingleCycle(array):
    # Write your code here.
    curr_indx = 0
    elements_visited = 0

    while(elements_visited < len(array)):
        if(elements_visited > 0 and curr_indx == 0):
            return False

        elements_visited += 1
        curr_indx = next_indx(curr_indx, array)

    return curr_indx == 0


def next_indx(curr_indx, array):
    jump = array[curr_indx]

    next_indx = (curr_indx + jump) % len(array)
    return next_indx


"""
[2, 3, 1, -4, -4, 2]

visited = 4
curr = 1
jump = -4
next = 1

Notes 
- Traverse through the array 
- Track the index that has been visited 


- Check if the current index already exists in the visited
	- if cycle ends at 0 > true else false 
- Add current index to visited 
- Jump to the index mentioned by the value of curr index 

8 item
curr_idx = 6 
jump = 13 

new_index = 1
curr


"""
