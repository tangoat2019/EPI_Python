def buy_and_sell_stock_once(stock):
    minium_so_far, max_profit = stock[0], 0
    for s in stock:
        minium_so_far = min(minium_so_far, s)
        max_profit = max(max_profit, s - minium_so_far)
    return max_profit
stock = [310,315,275,295,260,270,290,230,255,250]
max_price= 0
print(buy_and_sell_stock_once(stock))