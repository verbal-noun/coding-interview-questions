def minNumberOfCoinsForChange(n, denoms):
    # Write your code here.
    min_change = [float('inf') for num in range(n+1)]

    min_change[0] = 0

    for denom in denoms:
        for amount in range(n+1):
            if denom <= amount:
                min_change[amount] = min(
                    min_change[amount], min_change[amount - denom] + 1)

    return min_change[n] if min_change[n] != float('inf') else -1
