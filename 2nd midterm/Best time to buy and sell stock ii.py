def max_profit(prices):
    total_profit = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1]:
            total_profit += prices[i] - prices[i - 1]
    return total_profit

input_str = input("Enter prices: ")
prices = list(map(int, input_str.split(',')))
profit = max_profit(prices)
print(f"Maximum Profit: {profit}")
