def numberOfWaysToMakeChange(n, denoms):
    # Write your code here.
    num_ways = [0 for i in range(n+1)]

    num_ways[0] = 1

    for denom in denoms:
        for amount in range(1, n+1):
            if denom <= amount:
                num_ways[amount] += num_ways[amount - denom]

    return num_ways[n]
