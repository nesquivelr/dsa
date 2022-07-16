def greedy_knapsack(objects, profits, weights):
    costs = [profit/weight for profit, weight in zip(profits, weights)]
    max_size = 15
    selected_items = []
    while max_size > 0 and objects:
        item_id = costs.index(max(costs))
        current_weight = weights[item_id]
        current_object = objects[item_id]
        objects.pop(item_id)
        profits.pop(item_id)
        weights.pop(item_id)
        costs.pop(item_id)
        if max_size - current_weight < 0:
            continue
        else:
            selected_items.append(current_object)
            max_size -= current_weight
    return selected_items

if __name__ == '__main__':
    objects = [ 1, 2, 3, 4, 5, 6, 7]
    profits = [10, 5, 15, 7, 6, 18, 3]
    weights = [2, 3, 5, 7, 1, 4, 1]
    print(greedy_knapsack(objects, profits, weights))
