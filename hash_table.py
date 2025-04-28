stock_prices={}
with open("E:\Machine Learning\python code\stock_prices.csv","r") as f:
    for line in f:
        token=line.split(',')
        day=token[0].strip()
        price=float(token[1].strip())
        stock_prices[day]=price

print(stock_prices)
print("stock price on marce 9 :",stock_prices['march 9'])