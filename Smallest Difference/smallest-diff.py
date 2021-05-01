def smallestDifference(array_one, array_two):
    # Write your code here.

    array_one.sort()
    array_two.sort()

    idx_one = 0
    idx_two = 0
    smallest = float("inf")
    current = float("inf")
    smallest_pair = []

    while(idx_one < len(array_one) and idx_two < len(array_two)):
        first_num = array_one[idx_one]
        second_num = array_two[idx_two]
        if(first_num < second_num):
            current = second_num - first_num
            idx_one += 1
        elif(second_num < first_num):
            current = first_num - second_num
            idx_two += 1
        else:
            return [first_num, second_num]

        if smallest > current:
            smallest = current
            smallest_pair = [first_num, second_num]

    return smallest_pair
