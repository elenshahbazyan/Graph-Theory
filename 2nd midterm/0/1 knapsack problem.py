def knapsack(weights, values, capacity):
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w],
                               dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]

def main():
    n = int(input("Enter number of items: "))
    weights = list(map(int, input("Enter weights separated by space: ").split()))
    values = list(map(int, input("Enter values separated by space: ").split()))
    capacity = int(input("Enter knapsack capacity: "))

    if len(weights) != n or len(values) != n:
        print("Number of weights/values does not match the number of items.")
        return

    max_value = knapsack(weights, values, capacity)
    print("Maximum value in knapsack:", max_value)

if __name__ =="__main__":
    main()
