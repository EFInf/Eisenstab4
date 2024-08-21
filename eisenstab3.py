# Bottom-up: with a loop and memoization
#

prices = [0,1,1,3,5,5,7,9,8,10,10]
best_cut_price = []
m = len(prices)

for n in range(m):
    best = prices[n]
    for i in range(1,n):
        if best_cut_price[i]+prices[n-i] > best:
            best = best_cut_price[i]+prices[n-i]
    best_cut_price.append(best)

for i in range(m):
    print(f"Best cut for rod of length {i}: {best_cut_price[i]}")