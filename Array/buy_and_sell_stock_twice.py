def buy_and_sell_stock_twice(stock):
    min_so_far, max_profit_1, max_profit_2, i1, i2 = stock[0], 0, 0, 0, 0
    for cnt in range(len(stock)):
        min_so_far = min(min_so_far, stock[cnt])
        price_sell_now = stock[cnt] - min_so_far
        if (price_sell_now > max_profit_2):
            if price_sell_now > max_profit_1:
                if cnt - i1 >= 1:
                    max_profit_1 = price_sell_now
            else:
                if (i2 == 0 and cnt - i1 >= 1) or (i2 > 0 and cnt - i2 >= 1):
                    max_profit_2 = price_sell_now
    return max_profit_1+ max_profit_2

stock = [310,315,275,295,260,270,290,230,255,250]
print(buy_and_sell_stock_twice(stock))
