def find_job_secuence(jobs: list[str], profits: list[int], deadlines: list[int]):
    n_jobs = len(jobs)
    n_deadlines = max(deadlines)
    schedule = [-1 for i in range(n_deadlines)]
    while -1 in schedule:
        max_profit_idx = profits.index(max(profits))
        if schedule[deadlines[max_profit_idx]-1] == -1:
            schedule[deadlines[max_profit_idx]-1] = jobs[max_profit_idx]
        else:
            for i in range(deadlines[max_profit_idx]-1):
                if schedule[i] == -1:
                    schedule[i] = jobs[max_profit_idx]
                    break
        profits[max_profit_idx] = -1
    return schedule


if __name__ == '__main__':
    jobs = [f'J{i}' for i in range(1,6)]
    profits = [20, 15, 10, 5, 1]
    deadlines = [2, 2, 1, 3, 3]
    print(find_job_secuence(jobs, profits, deadlines))
    jobs = [f'J{i}' for i in range(1,8)]
    profits = [35, 30, 25, 20, 15, 12, 5]
    deadlines = [3, 4, 4, 2, 3, 1, 2]
    print(find_job_secuence(jobs, profits, deadlines))
