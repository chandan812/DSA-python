"""
GREEDY ALGORITHMS - Make locally optimal choice
"""

def activity_selection(start, finish):
    activities = sorted(zip(start, finish), key=lambda x: x[1])
    selected = [activities[0]]
    for i in range(1, len(activities)):
        if activities[i][0] >= selected[-1][1]:
            selected.append(activities[i])
    return len(selected)

def fractional_knapsack(weights, values, capacity):
    items = sorted(zip(values, weights), key=lambda x: x[0]/x[1], reverse=True)
    total_value = 0
    for value, weight in items:
        if capacity >= weight:
            total_value += value
            capacity -= weight
        else:
            total_value += value * (capacity / weight)
            break
    return total_value

def job_sequencing(jobs):
    jobs.sort(key=lambda x: x[2], reverse=True)
    max_deadline = max(job[1] for job in jobs)
    slots = [-1] * max_deadline
    total_profit = 0
    for job_id, deadline, profit in jobs:
        for j in range(min(max_deadline, deadline) - 1, -1, -1):
            if slots[j] == -1:
                slots[j] = job_id
                total_profit += profit
                break
    return total_profit

def huffman_encoding(freq):
    import heapq
    heap = [[weight, [char, ""]] for char, weight in freq.items()]
    heapq.heapify(heap)
    while len(heap) > 1:
        lo = heapq.heappop(heap)
        hi = heapq.heappop(heap)
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
    return sorted(heap[0][1:], key=lambda p: (len(p[-1]), p))

def min_platforms(arrivals, departures):
    arrivals.sort()
    departures.sort()
    platforms = 1
    max_platforms = 1
    i = j = 1
    while i < len(arrivals):
        if arrivals[i] <= departures[j-1]:
            platforms += 1
            i += 1
        else:
            platforms -= 1
            j += 1
        max_platforms = max(max_platforms, platforms)
    return max_platforms

if __name__ == "__main__":
    print(f"Activity Selection: {activity_selection([1, 3, 0, 5, 8, 5], [2, 4, 6, 7, 9, 9])}")
    print(f"Fractional Knapsack: {fractional_knapsack([10, 20, 30], [60, 100, 120], 50)}")
    print(f"Job Sequencing: {job_sequencing([('a', 2, 100), ('b', 1, 19), ('c', 2, 27)])}")
    print(f"Min Platforms: {min_platforms([900, 940, 950], [910, 1200, 1120])}")
