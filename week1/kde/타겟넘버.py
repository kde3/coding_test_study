def solution(numbers, target):
    def dfs(i, t):
        if i == len(numbers):
            return 1 if t == 0 else 0
        return dfs(i + 1, t + numbers[i]) + dfs(i + 1, t - numbers[i])

    return dfs(0, target)