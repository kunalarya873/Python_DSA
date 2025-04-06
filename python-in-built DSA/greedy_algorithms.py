#greedy

def fractional_knapsack (weights, values, capacity):
    n = len(weights)
    value_per_weight = [(values[i] / weights[i], weights[i], values[i]) for i in range(n)]
    value_per_weight.sort(reverse=True)
    total_value = 0
    remaining_capacity = capacity
    for vpw, w, v in value_per_weight:
        if w <- remaining_capacity:
            total_value += v
            remaining_capacity -= w
        else:
            fraction = remaining_capacity / w
            total_value += fraction * v
            break
    return total_value
weights=[5, 25, 35]
values=[60, 100, 120]
capacity = 50
max_profit=fractional_knapsack (weights, values, capacity)
print(max_profit)