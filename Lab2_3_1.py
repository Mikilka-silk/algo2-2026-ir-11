def max_hamsters(S, C, hamsters):
    low = 0
    high = C
    max_count = 0

    while low <= high:
        mid = (low + high) // 2
        if mid == 0:
            max_count = max(max_count, mid)
            low = mid + 1
            continue

        costs = []
        for hunger_norm, greed in hamsters:
            cost = hunger_norm + greed * (mid - 1)
            costs.append(cost)

        costs.sort()

        needed_food_total = sum(costs[:mid])

        if needed_food_total <= S:
            max_count = mid
            low = mid + 1
        else:
            high = mid - 1
            
    return max_count
