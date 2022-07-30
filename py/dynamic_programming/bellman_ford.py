import math

def bellman_ford(edges: list[int], start: int,  n: int):
    weights = [math.inf]*n
    weights[start] = 0
    for _ in range(n):
        changes = 0
        for start, end, cost in edges:
            new_value = weights[start]+cost 
            if new_value < weights[end]:
                weights[end] = new_value 
                changes += 1
        if not changes:
            break
    return weights

if __name__ == '__main__':
    edges = [
        (1, 2, 6),
        (1, 3, 5),
        (1, 4, 5),
        (2, 5, -1),
        (3, 2, -2),
        (3, 5, 1),
        (4, 3, -2),
        (4, 6, -1),
        (5, 7, 3),
        (6, 7, 3),
    ]
    weights = bellman_ford(edges, 1, 8)
    print(weights)
