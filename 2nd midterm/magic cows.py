MAX_DAYS = 50

def build_dp(C):
    dp = [[0] * (C + 1) for _ in range(MAX_DAYS + 1)]
    for cows in range(C + 1):
        dp[0][cows] = 1
    for day in range(1, MAX_DAYS + 1):
        for cows in range(C + 1):
            doubled = cows * 2
            if doubled <= C:
                dp[day][cows] = dp[day - 1][doubled]
                continue
            full, rest = divmod(doubled, C)
            farms = full * dp[day - 1][C]
            if rest:
                farms += dp[day - 1][rest]
            dp[day][cows] = farms
    return dp

def main():
    from sys import stdin
    data = [int(x) for x in stdin.read().strip().split()]
    if not data:
        return
    C, N, M = data[:3]
    idx = 3
    initial_cows = data[idx:idx + N]
    idx += N
    queries = data[idx:idx + M]
    dp = build_dp(C)
    answers = [0] * (MAX_DAYS + 1)
    for day in range(MAX_DAYS + 1):
        answers[day] = sum(dp[day][c] for c in initial_cows)
    for day in queries:
        print(answers[day])

if __name__ == "__main__":
    main()
