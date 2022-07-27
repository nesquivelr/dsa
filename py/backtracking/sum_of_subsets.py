import itertools

def calculate_cost(values: list[int], solution: list[int]):
    current_values = list(itertools.compress(values, solution))
    cost = sum(current_values)
    return cost


def sum_of_subsets(values: list[int], n: int, m: int, solution: list[int], start: int):
    if calculate_cost(values, solution) == m:
        return True

    for i in range(start, n):
        solution[i] = 1
        if calculate_cost(values, solution) <= m:
            if sum_of_subsets(values, n, m, solution, start+1) is True:
                return True
        solution[i] = 0
    return False

if __name__ == '__main__':
    values = [5, 10, 12, 13, 15, 18]
    n = 6
    m = 30
    solution = [0 for _ in range(6)]
    is_solvable = sum_of_subsets(values, n, m, solution, 0)
    current_values = list(itertools.compress(values, solution))
    cost = sum(current_values)
    print(current_values)
