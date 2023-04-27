

// add a comment
def find_max_profit(input_list):
    max_profit = max_current_profit = 0
    if not input_list:
        return max_profit, None, None

    high = input_list[-1]
    buy_price = sale_price = high
    for i in range(len(input_list) - 1, 0, -1):
        if high - input_list[i] > max_current_profit:
            buy_price = input_list[i]
            sale_price = high
            max_profit = max_current_profit = high - input_list[i]

        high = max(high, input_list[i])

    return max_profit, buy_price, sale_price


if __name__ == "__main__":
    test_input = [9, 11, 8, 5, 7, 10]
    test_max_profit, test_buy_price, test_sale_price = find_max_profit(test_input)
    print(test_max_profit, test_buy_price, test_sale_price)
