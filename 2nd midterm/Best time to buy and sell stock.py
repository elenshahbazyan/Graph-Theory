def best_time_to_buy_and_sell(prices):
    if not prices or len(prices) < 2:
        return 0, -1, -1

    min_price = prices[0]
    min_index = 0
    max_profit = 0
    buy_day = sell_day = 0

    for i in range(1, len(prices)):
        if prices[i] < min_price:
            min_price = prices[i]
            min_index = i
        elif prices[i] - min_price > max_profit:
            max_profit = prices[i] - min_price
            buy_day = min_index
            sell_day = i

    return max_profit, buy_day, sell_day

input_str = input("Enter prices: ")
prices = list(map(int, input_str.split(',')))

profit, buy, sell = best_time_to_buy_and_sell(prices)

if profit > 0:
    print(f"Maximum Profit: {profit}")
    print(f"Buy on day {buy} (price={prices[buy]})")
    print(f"Sell on day {sell} (price={prices[sell]})")
else:
    print("No profit.")
